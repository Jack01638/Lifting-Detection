##### Libraries #####
import numpy as np
import cv2
import mediapipe as mp
import copy


### Init Variables
stage = None
completed = False

# Exercises, Sets and Reps
rep_dict = {}
rep_dict["Bicep Curl"] = [6,10]

# Create copy of dict for reference numbers
rep_info_dict = copy.deepcopy(rep_dict)



##### Functions #####
def calculate_angle(a,b,c):
    a = np.array(a) # End point 1
    b = np.array(b) # Mid point
    c = np.array(c) # End point 2
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])   # Angle in radians
    angle = np.abs(radians*180.0/np.pi)                                             # Convert radians to degrees
    
    if angle > 180.0:   # If joints wrong way around, correct the values
        angle = 360-angle
        
    return angle


def CheckComplete(rep_dict, exercise):
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
    

# Exercises #variables that are not defined inside function or passed into may be causing issues for module
def BicepCurl(results, mp_pose, stage, completed):
    # Set exercise to reference in dict
    exercise = "Bicep Curl"

    # Joint landmarks
    landmarks = results.pose_landmarks.landmark
    
    # Get coordinates of joints
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

    # Calculate angles
    angle = calculate_angle(shoulder, elbow, wrist)
    
    # Visualize angles
    cv2.putText(image, str(angle), 
                   tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    # Counting reps
    if angle > 160: # Arm is extended
        stage = "down"
    if angle < 45 and stage == "down" and completed == False: # Arm is flexed and exercise not complete
        stage = "up"      
        completed = CheckComplete(rep_dict,exercise) # Return true if complete
        print(rep_dict) # Display dictionary
    
    return stage, completed


def Row(results, mp_pose, stage, completed):
    # Set exercise to reference in dict
    exercise = "Row"
    
    # Joint landmarks
    landmarks = results.pose_landmarks.landmark
    
    # Get coordinates
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

    # Calculate angles and heights
    angle1 = calculate_angle(shoulder, hip, knee)                           # Check if bent over at waist
    #elbow_height = elbow[1] #landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y       # Height of elbow
    #hip_height = hip[1] #landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y           # Height of hips
    #shoulder_height = shoulder[1] #landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y    # height of shoulder

    # Visualize angles and heights
    cv2.putText(image, str(angle1),   
                   tuple(np.multiply(hip, [640, 480]).astype(int)), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(image, str(elbow[1]),   
                   tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    # Counting reps
    if elbow[1] > hip[1]: # Elbow is below hip height (height values reversed)
        stage = "down"
    if  angle1 < 150 and elbow[1] < hip[1] and elbow[1] <= (shoulder[1] + 0.05) and stage == "down" and completed == False: # Bent Forwards, elbow above hip
        stage = "up"                                                                                                                        # Elbow above shoulder (with 0.05 leniency)
        completed = CheckComplete(rep_dict,exercise)
        print(rep_dict)
    
    return stage, completed 


def Squat(results, mp_pose, stage, completed):
    exercise = "Squat"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


def ShoulderPress(results, mp_pose, stage, completed):
    exercise = "Shoulder Press"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


def TricepExtension(results, mp_pose, stage, completed):
    exercise = "Tricep Extension"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


def BenchPress(results, mp_pose, stage, completed):
    exercise = "Bench Press"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


def ChestFlye(results, mp_pose, stage, completed):
    exercise = "Chest Flye"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


def SideRaise(results, mp_pose, stage, completed):
    exercise = "Side Raise"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


def CalfRaise(results, mp_pose, stage, completed):
    exercise = "Calf Raise"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


def Shrug(results, mp_pose, stage, completed):
    exercise = "Shrug"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


def Deadlift(results, mp_pose, stage, completed):
    exercise = "Deadlift"
    landmarks = results.pose_landmarks.landmark

    # Get coordinates

    # Calculate angles / positions

    # Visualise / display angles

    ##### counting reps #####

    
    return stage, completed


##### Mediapipe Tracking & Detection #####
### Mediapipe Variables
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

### Start Video Feed
cap = cv2.VideoCapture(0)

## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.8) as pose: #start tracking and detection
    while cap.isOpened(): #while video feed is on
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            ### function calling for left bicep curl ###
            stage, completed = BicepCurl(results,mp_pose,stage,completed)
           #stage, row_count = Row(results,mp_pose,row_count,stage)
            
        except: #not a major problem if passes, i think this will apply to only the 1 frame
            pass
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
