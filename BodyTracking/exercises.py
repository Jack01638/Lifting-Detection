import numpy as np
import cv2
import mediapipe as mp


def calculate_angle(a,b,c):
    a = np.array(a) # End point 1
    b = np.array(b) # Mid point
    c = np.array(c) # End point 2
    ########ERROR IN HERE
    rads = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])   # Angle in radians
    angle = np.abs(rads*180.0/np.pi)                                             # Convert radians to degrees
    #########
    if angle > 180.0:   # If joints wrong way around, correct the values
        angle = 360-angle

    return angle


def CheckComplete(rep_dict, exercise,rep_info_dict):
    completed = False

    # Count down reps
    if rep_dict[exercise][0] >= 0 and rep_dict[exercise][1] > 0:
        rep_dict[exercise][1] -= 1

    # Count down sets and reset reps
    if rep_dict[exercise][1] < 1 and rep_dict[exercise][0] > 0:
        rep_dict[exercise][0] -= 1
        rep_dict[exercise][1] = rep_info_dict[exercise][1]

    # Set exercise as complete
    if rep_dict[exercise][0] == 0 and rep_dict[exercise][1] == 0:
        completed = True
        
    return completed
    

# Exercises
def BicepCurl(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict):
    # Set exercise to reference in dict
    exercise = "Bicep Curl"
    
    # Get coordinates of joints
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    
    # Calculate angles
    angle = calculate_angle(shoulder, elbow, wrist)

    # Counting reps
    if angle > 160: # Arm is extended
        stage = "down"
    if angle < 45 and stage == "down" and completed == False: # Arm is flexed and exercise not complete
        stage = "up"      
        completed = CheckComplete(rep_dict,exercise,rep_info_dict) # Return true if complete
        print(rep_dict) # Display dictionary
    
    return stage, completed