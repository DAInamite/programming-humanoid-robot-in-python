'''In this exercise you need to use the learned classifier to recognize current posture of robot

* Tasks:
    1. load learned classifier in `PostureRecognitionAgent.__init__`
    2. recognize current posture in `PostureRecognitionAgent.recognize_posture`

* Hints:
    Let the robot execute different keyframes, and recognize these postures.

'''

from angle_interpolation import AngleInterpolationAgent

from keyframes import hello
from keyframes import leftBackToStand 
from keyframes import rightBackToStand
from keyframes import wipe_forehead

# to check not working: rightBellyToStand / leftBellyToStand
from keyframes import leftBellyToStand
from keyframes import rightBellyToStand 

import pickle as pickle
from os import listdir, path
import numpy as np

ROBOT_POSE_CLF = 'robot_pose.pkl'
ROBOT_POSE_DATA_DIR = 'robot_pose_data'
    
class PostureRecognitionAgent(AngleInterpolationAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(PostureRecognitionAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        self.posture = 'unknown'
        self.class_postures = listdir(ROBOT_POSE_DATA_DIR)
        ## get the classigier
        self.posture_classifier = pickle.load(open(ROBOT_POSE_CLF,'rb')) # LOAD YOUR CLASSIFIER
        
    def think(self, perception):
        self.posture = self.recognize_posture(perception)
        return super(PostureRecognitionAgent, self).think(perception)

    def recognize_posture(self, perception):
        posture = 'unknown'
        # YOUR CODE HERE
        
        data = []
        data.append(perception.joint['LHipYawPitch'])
        data.append(perception.joint['LHipRoll'])
        data.append(perception.joint['LHipPitch'])
        data.append(perception.joint['LKneePitch'])
        data.append(perception.joint['RHipYawPitch'])
        data.append(perception.joint['RHipRoll'])
        data.append(perception.joint['RHipPitch'])
        data.append(perception.joint['RKneePitch'])
        # AngleX
        data.append(perception.imu[0])
        # AngleY
        data.append(perception.imu[1])
        
        data = np.array(data).reshape(1, -1)
        
        index = self.posture_classifier.predict(data)
        posture =  self.class_postures[index[0]]
        return posture

if __name__ == '__main__':
    agent = PostureRecognitionAgent()
    agent.keyframes = rightBackToStand()  # CHANGE DIFFERENT KEYFRAMES 
    
    agent.run()
