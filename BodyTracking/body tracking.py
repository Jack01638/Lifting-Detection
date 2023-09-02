##### Libraries #####
import numpy as np
import cv2
import mediapipe as mp
import copy
from exercises import *


### Init Variables
stage = None
completed = False
rep_dict = (
    {}
)  # exercise names in rep dict must match exercise variable names in exercise functions


# Exercises, Sets and Reps
"""
### Asking for and Setting up reps and sets

    check for saved file:
    if yes saved file:
        what do you want to do?
        Use saved file - Edit Saved File - Delete Saved File - Exit Program
        if use saved file:
            continue to tracking and reps
        if edit saved file:
            #selecting which exercise to edit
            return back to what do you want to do?
        if delete saved file:
            are you sure?
            yes:
                delete saved file
                continue to set up sets and reps
            no:
                return back to what do you want to do?
        if exit program:
            exit program
    if no saved file:
        set up sets and reps
###
"""
#Push Day
rep_dict["Bench Press"] = [7,20]            #6 sets of 15
rep_dict["Shoulder Press"] = [5,12]         #6 sets of 12
rep_dict["Tricep Extension"] = [5,12]       #6 sets of 12
rep_dict["Chest Flye"] = [4,12]             #5 sets of 12

#Pull Day
rep_dict["Row"] = [9, 15]                   #10 sets of 15
rep_dict["Bicep Curl"] = [7, 12]            #8 sets of 12
rep_dict["Lateral Side Raise"] = [5,8]      #6 sets of 8
rep_dict["Dumbbell Shrug"] = [5,15]         #6 sets of 15

#Leg Day
rep_dict["Standing Calf Raises"] = [7,30]   #8 sets of 30
rep_dict["Squat"] = [5, 12]                 #6 sets of 12
rep_dict["Deadlift"] = [5,12]               #6 sets of 12
rep_dict["Romanian Deadlift"] = [5,15]      #6 sets of 15

# Create deep copy of dict for reference numbers
rep_info_dict = copy.deepcopy(rep_dict)


##### Mediapipe Tracking & Detection #####
### Mediapipe Variables
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

### Start Video Feed
cap = cv2.VideoCapture(0)

## Setup mediapipe instance
with mp_pose.Pose(
    min_detection_confidence=0.8, min_tracking_confidence=0.8) as pose:  # start tracking and detection
    while cap.isOpened():  # while video feed is on
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)
        try:
            landmarks = results.pose_landmarks.landmark
        except:
            pass
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks
        try:
            ### Exercise Function HERE ### (will depend on training plan etc)
            stage, completed = BicepCurl(
                landmarks, mp_pose, stage, completed, rep_dict, rep_info_dict)
            ###          ###           ###

        except:
            pass

        # Render detections
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
        )

        cv2.imshow("Mediapipe Feed", image)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
