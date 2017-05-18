'''
'''

import sys
import unittest
from mock import patch
from cStringIO import StringIO
from contextlib import contextmanager
import random


class TestGetSensorData(unittest.TestCase):
    @patch('spark_agent.SparkAgent.__init__', lambda i: None)  # no connection to simspark
    @contextmanager  # temporarily manage sys.stdout
    def test(self):
        out, sys.stdout = sys.stdout, StringIO()
        from get_sensor_data import MyAgent
        from spark_agent import Perception

        angle = random.random()
        temperature = random.random()
        perception = Perception()
        perception.joint['HeadYaw'] = angle
        perception.joint_temperature['HeadYaw'] = temperature

        agent = MyAgent()
        agent.think(perception)
        sys.stdout.seek(0)
        your_answer = sys.stdout.readline()

        sys.stdout.truncate(0)
        print 'HeadYaw angle: ' + str(angle) + ' temperature: ' + str(temperature)
        sys.stdout.seek(0)
        correct_answer = sys.stdout.readline()
        self.assertEqual(your_answer, correct_answer)


if __name__ == '__main__':
    unittest.main()
