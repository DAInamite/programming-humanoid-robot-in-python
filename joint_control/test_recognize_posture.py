import unittest
from mock import patch, MagicMock

import pickle

from recognize_posture import PostureRecognitionAgent
from spark_agent import Perception, JOINT_CMD_NAMES
from os import listdir, path
import numpy as np

ROBOT_POSE_DATA_DIR = 'robot_pose_data'


def init_agent(agent):
    perception = Perception()

    for j in JOINT_CMD_NAMES.keys():
        perception.joint[j] = 0

    agent.perception = perception


class TestAngleInterpolation(unittest.TestCase):
    @patch('spark_agent.SparkAgent.__init__', lambda self, simspark_ip, simspark_port, teamname, player_id, sync_mode: init_agent(self))  # no connection to simspark
    def setUp(self):
        self.agent = PostureRecognitionAgent()

    def _set_joint_to_zero(self):
        # all zero
        for k in self.agent.perception.joint.keys():
            self.agent.perception.joint[k] = 0

    def test_zero(self):
        self._set_joint_to_zero()
        self.agent.perception.imu = [0, 0]

        p = self.agent.recognize_posture(self.agent.perception)
        self.assertEqual(p, 'Stand')

    def test_belly(self):
        self._set_joint_to_zero()
        self.agent.perception.imu = [0, 1.7]

        p = self.agent.recognize_posture(self.agent.perception)
        self.assertEqual(p, 'Belly')

    def test_back(self):
        self._set_joint_to_zero()
        self.agent.perception.imu = [0, -1.7]

        p = self.agent.recognize_posture(self.agent.perception)
        self.assertEqual(p, 'Back')

    def test_left(self):
        self._set_joint_to_zero()
        self.agent.perception.imu = [-1.7, 0]

        p = self.agent.recognize_posture(self.agent.perception)
        self.assertEqual(p, 'Left')

    def test_right(self):
        self._set_joint_to_zero()
        self.agent.perception.imu = [1.7, 0]

        p = self.agent.recognize_posture(self.agent.perception)
        self.assertEqual(p, 'Right')

    def test_knee(self):
        self._set_joint_to_zero()
        self.agent.perception.imu = [0, 0]
        self.agent.perception.joint['LKneePitch'] = 3
        self.agent.perception.joint['RKneePitch'] = 3

        p = self.agent.recognize_posture(self.agent.perception)
        self.assertEqual(p, 'Knee')

    def _load_pose_data(self, c):
        '''load pose data from file'''
        filename = path.join(ROBOT_POSE_DATA_DIR, c)
        data = pickle.load(open(filename))
        return data

    def test_dataset(self):
        self._set_joint_to_zero()
        classes = listdir(ROBOT_POSE_DATA_DIR)
        joint_names = ['LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch']

        n = 0
        e = 0
        for c in classes:
            data = self._load_pose_data(c)
            for d in data:
                for i in range(len(d) - 2):
                    self.agent.perception.joint[joint_names[i]] = d[i]  # joint angles
                self.agent.perception.imu = d[-2:]

                p = self.agent.recognize_posture(self.agent.perception)
                if p != c:
                    e += 1
                n += 1

        with open("test_recognize_posture.txt", 'w') as f:
            f.write("%d / % d" % (e, n))

if __name__ == '__main__':
    unittest.main()
