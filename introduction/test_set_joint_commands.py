'''
'''

import unittest
from mock import patch


class TestGetSensorData(unittest.TestCase):
    @patch('spark_agent.SparkAgent.__init__', lambda i: None)  # no connection to simspark
    def test(self):
        from get_sensor_data import MyAgent
        from spark_agent import Perception

        perception = Perception()

        agent = MyAgent()
        action = agent.think(perception)

        self.assertEqual(action.stiffness['LShoulderPitch'], 0)
        self.assertEqual(action.speed['HeadYaw'], 0.1)


if __name__ == '__main__':
    unittest.main()
