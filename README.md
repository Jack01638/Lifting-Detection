# Lifting Detection

An application to track body movements in order to count exercise repetitions performed.

All movements are tracked using the mediapipe python library. It uses pose prediction in order to predict where joints and limbs are through a live camera feed from which angles and motions are calculated in order to check when a full repetition of a specific exercise is completed.

## Libraries Used:

- Mediapipe
- Numpy
- CV2
- copy
- exercises.py (custom built library for this application to store exercise functions)

## Future Updates Planned:
- Finish all exercise functions
- Add options menu on startup
    - see "lifting tracking.drawio" file for Main Menu details
- Save files for storing reps / sets for each exercise
- Delay and onscreen countdown before detection starts
    - This will allow athlete to get into position and prevent mistaken rep counts when athlete is moving into position
- Tweak and play with detection parameters for increased accuracy while taking into account usability
- Add generalistion to allow for different body types to use
    - e.g. bicep curl requires hand to move below hip to count as "down". Someone with short arms may not be able to do this. Generalised movement / allowing users to perform their own reps to setup the app, software tracks movement parameters and stores theses in same file as rep/set file
