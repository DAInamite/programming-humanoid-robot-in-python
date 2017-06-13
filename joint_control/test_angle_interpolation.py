import unittest
from mock import patch, MagicMock
import numpy as np
from angle_interpolation import AngleInterpolationAgent
from spark_agent import Perception, JOINT_CMD_NAMES

start_time = 1000


def init_agent(agent):
    perception = Perception()
    perception.time = start_time

    for j in JOINT_CMD_NAMES.keys():
        perception.joint[j] = 0

    agent.perception = perception

class TestAngleInterpolation(unittest.TestCase):
    @patch('spark_agent.SparkAgent.__init__', lambda self, simspark_ip, simspark_port, teamname, player_id, sync_mode: init_agent(self))  # no connection to simspark
    def test(self):
        from keyframes import hello, leftBackToStand
        agent = AngleInterpolationAgent()
        keyframes = leftBackToStand()

        keyframes_time = np.max([t[-1] for t in keyframes[1]])

        perception = agent.perception
        trajectory_t = []
        trajectory = []

        while perception.time < keyframes_time + start_time:
            agent.perception = perception
            target_joints = agent.angle_interpolation(keyframes, perception)
            trajectory.append(target_joints)
            trajectory_t.append(perception.time - start_time)
            perception.time += 0.01

        # check error in keyframe point
        error_at_key_frame = []
        for i in range(len(keyframes[0])):
            n = keyframes[0][i]
            if n in ['LWristYaw', 'RWristYaw', 'LHand', 'RHand']:  # ignore some joints
                continue

            for j in range(len(keyframes[1][i])):
                t = keyframes[1][i][j]
                for ti in range(len(trajectory_t)):
                    tt = trajectory_t[ti]
                    if abs(t - tt) < 0.005:
                        e = trajectory[ti][n] - keyframes[2][i][j][0]
                        error_at_key_frame.append(e)

        with open("test_angle_interpolation.txt", 'w') as f:
            f.write(str(np.mean(np.abs(error_at_key_frame))))


if __name__ == '__main__':
    unittest.main()