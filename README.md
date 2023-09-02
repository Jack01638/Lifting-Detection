# Lifting Detection

An application to track body movements in order to count exercise repetitions performed.

All movements are tracked using the mediapipe python library. It uses pose prediction in order to predict where joints and limbs are through a live camera feed from which angles and motions are calculated in order to check when a full repetition of a specific exercise is completed.

## Libraries used:

- Mediapipe
- Numpy
- CV2
- copy
- exercises.py (custom built library for this application to store exercise functions)
