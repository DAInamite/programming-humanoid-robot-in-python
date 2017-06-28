import unittest
from mock import patch, MagicMock
import numpy as np
from math import cos, sin
from forward_kinematics import ForwardKinematicsAgent
from spark_agent import Perception, JOINT_CMD_NAMES
import json
import functools


def trans_matrix(x, y, z, wx, wy, wz):
    '''create transform matrix from position and rotation
    '''
    cz = cos(wz)
    sz = sin(wz)
    cy = cos(wy)
    sy = sin(wy)
    cx = cos(wx)
    sx = sin(wx)
    czcy = cz * cy
    czsy = cz * sy
    szcy = sz * cy
    szsy = sz * sy
    M = np.asarray([[czcy, -sz * cx + czsy * sx, sz * sx + czsy * cx, x],
                    [szcy, cz * cx + szsy * sx, -cz * sx + szsy * cx, y],
                    [-sy, cy * sx, cx * cy, z],
                    [0, 0, 0, 1]])
    return M


def init_agent(agent):
    perception = Perception()
    perception.time = 0

    for j in JOINT_CMD_NAMES.keys():
        perception.joint[j] = 0

    agent.perception = perception


with open('fk_samples.json') as f:
    samples = json.load(f)


class TestForwardKinematics(object):
    @patch('spark_agent.SparkAgent.__init__', lambda self, simspark_ip, simspark_port, teamname, player_id, sync_mode: init_agent(self))  # no connection to simspark
    def setUp(self):
        self.agent = ForwardKinematicsAgent()
        self.samples = samples

    def check_forward_kinematics(self, pname, end_effector):
        self.setUp()

        joint_names = self.samples['joint_names']
        angles = self.samples[pname]['angles']
        joints = dict(zip(joint_names, angles))
        self.agent.perception.joint.update(joints)

        self.agent.think(self.agent.perception)

        positions = self.samples[pname]['positions']
        for i, n in enumerate(self.samples['names']):
            if n == end_effector:
                p = positions[i]
                Tr = trans_matrix(*p)
                T = self.agent.transforms[n]
                assert np.allclose(T, Tr)


t = TestForwardKinematics()


def test_generator():
    for pname in ['init', 'moveInit', 'rest']:
        for end_effector in samples['names']:
            yield t.check_forward_kinematics, pname, end_effector


if __name__ == '__main__':
    unittest.main()
