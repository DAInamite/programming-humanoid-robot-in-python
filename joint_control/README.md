# 3: Joint Control
## PID Controller for Joint Servo
1. complete the implementation of PID controller in [pid.py](./pid.py)
2. use [pid_test.ipynb](./pid_test.ipynb) to tuning PID parameters
	* start ```jupyter notebook``` in this folder, then you can launch [pid_test.ipynb](./pid_test.ipynb) in your web browser
    * follow instruction in notebook, run the code and tune PID parameters
3. save the best parameters in ```__init__``` of ```class PIDController```

## Keyframe Motion
1. implement angle interploation method by using splins interpolation or Bezier interpolation in file [angle_interpolation.py](./angle_interpolation.py), please follow instruction in the comments of the file.
    * run simspark and [angle_interpolation.py](./angle_interpolation.py) to test [hello](./keyframes/hello.py) motion
2. test your implementation with provided keyframes in [keyframes](./keyframes) folder， for example:
    * import keyframe with ```from keyframes import hello```
    * and set the keyframe in ```main``` function, e.g. ```agent.keyframes = hello()```
    * Note: the provided keyframes doesn't have joint `RHipYawPitch`, please set `RHipYawPitch` as `LHipYawPitch` which reflects the real robot.
3. (optional) create your own keyframes

## Posture Recognition
use machine learning to recognize robot's posture [learn_posture.ipynb](./learn_posture.ipynb), the [scikit-learn-intro.ipynb](./scikit-learn-intro.ipynb) is a good example to follow.

1. preparing dataset (step 1~2 in [learn_posture.ipynb](./learn_posture.ipynb) )
2. traning dataset, and save the results (step 3~5 in [learn_posture.ipynb](./learn_posture.ipynb) )
3. getting feature data from simulation and recognize current posture in [recognize_posture.py](./recognize_posture.py)
4. if the result is not good in simulation, adding new train data with [add_training_data.ipynb](add_training_data.ipynb)
5. commit file *robot_pose.pkl* as trained result to git before submission.

### Automonous standing up
1. complete the [standing_up.py](./standing_up.py), e.g. call keyframe motion corresponds to current posture
2. Test with the ```TestStandingUpAgent``` which turns off all joints regularly to make the robot falls
3. (optional) The ```TestStandingUpAgent``` always falls to belly, please also test other suitations: e.g. execute a keyframe motion to make robot falls to another pose and let it stands up.
