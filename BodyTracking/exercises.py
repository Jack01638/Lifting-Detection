##### Libraries #####
import numpy as np


### Misc. functions
def calculate_angle(a, b, c):
    a = np.array(a)  # End point 1
    b = np.array(b)  # Mid point
    c = np.array(c)  # End point 2

    rads = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])  # Angle in radians
    angle = np.abs(rads * 180.0 / np.pi)  # Convert radians to degrees

    if angle > 180.0:  # If joints wrong way around, correct the values
        angle = 360 - angle

    return angle


def CheckComplete(rep_dict, exercise, rep_info_dict):
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


def Display(rep_dict, rep_info_dict, exercise):
    print(
"""Exercise: {}
Sets Left {} / {}
Reps Left {} / {}
""".format(
            exercise,
            rep_dict[exercise][0],
            rep_info_dict[exercise][0],
            rep_dict[exercise][1],
            rep_info_dict[exercise][1],)
    )

    return 0


##### Exercises #####
""" ### Generalised function for each exercise ###

def (landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict): #add function name
    # Set exercise to reference in dict
    exercise = "" #add exercise name

    # Get coordinates of joints
    #add join name and joint reference
    #https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
    joint = [landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].x,landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].y]

    # Calculate angles
    angle = calculate_angle(joint1, joint2, joint3) #add joint names

    # Counting reps
    if ? : #add condition for "down" stage
        stage = "down"
    if ? and stage == "down" and completed == False: #add conditions for "up" stage
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)

    return stage, completed
    
"""


def BicepCurl(landmarks, mp_pose, stage, completed, rep_dict, rep_info_dict):
    # Set exercise to reference in dict
    exercise = "Bicep Curl"

    # Get coordinates of joints
    shoulder = [
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,]
    elbow = [
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,]
    wrist = [
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,]

    # Calculate angles
    angle = calculate_angle(shoulder, elbow, wrist)

    # Counting reps
    if angle > 160:
        stage = "down"
    if angle < 45 and stage == "down" and completed == False:
        stage = "up"
        completed = CheckComplete(rep_dict, exercise, rep_info_dict)
        Display(rep_dict, rep_info_dict, exercise)

    return stage, completed


def Squat(landmarks, mp_pose, stage, completed, rep_dict, rep_info_dict):
    # Set exercise to reference in dict
    exercise = "Squat"

    # Get coordinates of joints
    shoulder = [
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,]
    hip = [
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,]
    knee = [
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,]
    ankle = [
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,]

    # Calculate angles
    angleUpper = calculate_angle(shoulder, hip, knee)
    angleLower = calculate_angle(hip, knee, ankle)

    # Counting reps
    if angleLower < 90 and angleUpper < 70:
        stage = "down"
    if angleLower > 160 and stage == "down" and completed == False:
        stage = "up"
        completed = CheckComplete(rep_dict, exercise, rep_info_dict)
        Display(rep_dict, rep_info_dict, exercise)

    return stage, completed


def Row(landmarks, mp_pose, stage, completed, rep_dict, rep_info_dict):
    # Set exercise to reference in dict
    exercise = "Row"

    # Get coordinates of joints
    shoulder = [
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,]
    hip = [
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,]
    knee = [
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,]
    wrist = [
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,]
    elbow = [
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,]

    # Calculate angles
    angle = calculate_angle(shoulder, hip, knee)

    # Counting reps
    if wrist[1] > hip[1]:
        stage = "down"
    if angle < 135 and elbow[1] <= shoulder[1] and stage == "down" and completed == False:
        stage = "up"
        completed = CheckComplete(rep_dict, exercise, rep_info_dict)
        Display(rep_dict, rep_info_dict, exercise)

    return stage, completed

def LatSideRaise(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict): 
    # Set exercise to reference in dict
    exercise = "Lateral Side Raise"

    # Get coordinates of joints
    shoulder = [
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    wrist = [
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,]
    hip = [
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,]
    knee = [
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,]
    

    # Calculate angles
    angle = calculate_angle(shoulder, hip, knee)

    # Counting reps
    if wrist[1] > hip[1]:
        stage = "down"
    if wrist[1] >= shoulder[1] and angle <= 160 and stage == "down" and completed == False:
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed

def ShoulderPress(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict):
    # Set exercise to reference in dict
    exercise = "Shoulder Press"

    # Get coordinates of joints
    ear = [
        landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y]
    wrist = [
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,]
    elbow = [
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,]
    shoulder = [
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,]

    # Calculate angles
    angle = calculate_angle(shoulder, elbow, wrist)

    # Counting reps
    if wrist[1] > ear[1]:
        stage = "down"
    if wrist[1] < ear[1] and angle > 165 and stage == "down" and completed == False:
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed


"""

def BenchPress(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict):
    # Set exercise to reference in dict
    exercise = "Bench Press" #add exercise name

    # Get coordinates of joints
    joint = [landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].x,landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].y]

    # Calculate angles
    angle = calculate_angle(joint1, joint2, joint3) #add joint names

    # Counting reps
    if ? : #add condition for "down" stage
        stage = "down"
    if ? and stage == "down" and completed == False: #add conditions for "up" stage
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed


def CalfRaise(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict):
    # Set exercise to reference in dict
    exercise = "Standing Calf Raise"

    # Get coordinates of joints
    joint = [landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].x,landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].y]

    # Calculate angles
    angle = calculate_angle(joint1, joint2, joint3) #add joint names

    # Counting reps
    if ? : #add condition for "down" stage
        stage = "down"
    if ? and stage == "down" and completed == False: #add conditions for "up" stage
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed


def ChestFlye(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict): 
    # Set exercise to reference in dict
    exercise = "Chest Flye" 

    # Get coordinates of joints
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    
    # Calculate angles
    angle = calculate_angle(shoulder,elbow,wrist) #add joint names

    # Counting reps
    if ? : #add condition for "down" stage
        stage = "down"
    if ? and stage == "down" and completed == False: #add conditions for "up" stage #wrists should be close together, arms should stay within angle range
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed


def Deadlift(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict):
    # Set exercise to reference in dict
    exercise = "Deadlift"

    # Get coordinates of joints
    #add join name and joint reference
    #https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
    joint = [landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].x,landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].y]

    # Calculate angles
    angle = calculate_angle(joint1, joint2, joint3) #add joint names

    # Counting reps
    if ? : #add condition for "down" stage
        stage = "down"
    if ? and stage == "down" and completed == False: #add conditions for "up" stage
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed


def Shrug(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict): 
    # Set exercise to reference in dict
    exercise = "Dumbbell Shrug" 

    # Get coordinates of joints
    joint = [landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].x,landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].y]

    # Calculate angles
    angle = calculate_angle(joint1, joint2, joint3) #add joint names

    # Counting reps
    if ? : #add condition for "down" stage
        stage = "down"
    if ? and stage == "down" and completed == False: #add conditions for "up" stage
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed


def TricepExtension(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict): 
    # Set exercise to reference in dict
    exercise = "Tricep Extension" 

    # Get coordinates of joints
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    

    # Calculate angles
    angle = calculate_angle(shoulder,elbow,wrist)

    # Counting reps
    if ? : #add condition for "down" stage
        stage = "down"
    if ? and stage == "down" and completed == False: #add conditions for "up" stage
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed


    def RDL(landmarks, mp_pose, stage, completed,rep_dict,rep_info_dict): 
    # Set exercise to reference in dict
    exercise = "Romanian Deadlift" 

    # Get coordinates of joints
    joint = [landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].x,landmarks[mp_pose.PoseLandmark."JOINT_REFERENCE".value].y]

    # Calculate angles
    angle = calculate_angle(joint1, joint2, joint3) #add joint names

    # Counting reps
    if ? : #add condition for "down" stage
        stage = "down"
    if ? and stage == "down" and completed == False: #add conditions for "up" stage
        stage = "up"
        completed = CheckComplete(rep_dict,exercise,rep_info_dict)
        Display(rep_dict,rep_info_dict,exercise)
        
    return stage, completed
    
"""
