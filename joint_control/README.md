# Week 2: Joint Control
## PID Controller for Joint Servo
1. complete the implementation of PID controller in [pid.py](./pid.py)
2. use [pid_test.ipynb](./pid_test.ipynb) to tuning PID parameters
	* start ```ipython notebook``` in this folder, then you can launch [pid_test.ipynb](./pid_test.ipynb) in your web browser
3. save the best parameters in ```__init__``` of ```class PIDController```

## Keyframe Motion
1. implement angle interploation method by using splins interpolation or Bezier interpolation in file [angle_interpolation.py](./angle_interpolation.py).
2. test your implementation with provided keyframes in *keyframes* folder
3. (optional) create your own keyframes

## Posture Recognition
use machine learning to recognize robot's posture (following the example in [scikit-learn-intro.ipynb](./scikit-learn-intro.ipynb)
1. preparing dataset (step 1~2 in [scikit-learn-intro.ipynb](./scikit-learn-intro.ipynb) )
	* the dateset are in *robot_pose_data* folder
	* each file contains the data belongs to this posture, e.g. the data in *Back* file are collected when robot was in "Back" posture
  * the data file can be load by ```pickle```, e.g. ```pickle.load(open('Back'))```, the data is a list of feature data
  * the features (e.g. each row of the data) are ['AngleX', 'AngleY', 'LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch'], where 'AngleX' and 'AngleY' are body angle and others are joint angles.
2. traning dataset, and save the results (step 3~5 in [scikit-learn-intro.ipynb](./scikit-learn-intro.ipynb) )
3. getting feature data from simulation and recognize current posture in [recognize_posture.py](./recognize_posture.py)

### Automonous standing up
