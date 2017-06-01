'''In this exercise you need to use the learned classifier to recognize current posture of robot

* Tasks:
    1. load learned classifier in `PostureRecognitionAgent.__init__`
    2. recognize current posture in `PostureRecognitionAgent.recognize_posture`

* Hints:
    Let the robot execute different keyframes, and recognize these postures.

'''


from angle_interpolation import AngleInterpolationAgent
from keyframes import leftBellyToStand
import pickle
from os import listdir, path
import numpy as np
from sklearn import svm, metrics





class PostureRecognitionAgent(AngleInterpolationAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(PostureRecognitionAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        self.posture = 'unknown'
        self.posture_classifier = pickle.load(open('robot_pose.pkl'))  # LOAD YOUR CLASSIFIER

    def think(self, perception):
        self.posture = self.recognize_posture(perception)
        return super(PostureRecognitionAgent, self).think(perception)

    def recognize_posture(self, perception):
        posture = 'unknown'
        # YOUR CODE HERE
	data_pos = []

	data_pos.append(perception.joint['LHipYawPitch'])
	data_pos.append(perception.joint['LHipRoll'])
	data_pos.append(perception.joint['LHipPitch'])
	data_pos.append(perception.joint['LKneePitch'])
	data_pos.append(perception.joint['RHipYawPitch'])
	data_pos.append(perception.joint['RHipRoll'])
	data_pos.append(perception.joint['RHipPitch'])
	data_pos.append(perception.joint['RKneePitch'])
	data_pos.append(perception.imu[0])
	data_pos.append(perception.imu[1])

	data_pos = np.array(data_pos).reshape(1, -1)

	posture = self.posture_classifier.predict(data_pos)

	print listdir('robot_pose_data')[posture[0]]
        return posture

if __name__ == '__main__':
    agent = PostureRecognitionAgent()
    agent.keyframes = leftBellyToStand()  # CHANGE DIFFERENT KEYFRAMES
    agent.run()
