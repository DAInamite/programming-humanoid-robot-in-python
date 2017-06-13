
from pid import PIDAgent
import numpy as np
import unittest


class PIDTestAgent(PIDAgent):
    def __init__(self):
        super(PIDTestAgent, self).__init__(player_id=1)

        self.test_trajectory = [0.0] * 100 + [1.0] * 100 + [-1.0] * 100
        self.test_trajectory *= 3
        self.target_requested = []
        self.sensor_value = []

    def think(self, perception):
        i = len(self.target_requested)
        joint_name = 'HeadYaw'
        if i < len(self.test_trajectory):
            v = self.test_trajectory[i]
            self.target_joints[joint_name] = v
            self.target_requested.append(v)
            self.sensor_value.append(perception.joint[joint_name])

        action = super(PIDTestAgent, self).think(perception)
        return action


class TestPID(unittest.TestCase):
    def test(self):
        agent = PIDTestAgent()
        while len(agent.test_trajectory) > len(agent.target_requested):
            agent.sense_think_act()

        t = np.asarray(agent.target_requested)
        s = np.asarray(agent.sensor_value)
        e = np.abs(t[:-1] - s[1:])
        with open("test_pid.txt", 'w') as f:
            f.write(str(np.mean(e)))

if __name__ == '__main__':
    unittest.main()
