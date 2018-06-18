'''
'''
# add PYTHONPATH
import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'software_installation'))
import unittest
from mock import patch, MagicMock


class TestSetJointCommands(unittest.TestCase):
    @patch('spark_agent.SparkAgent.__init__', lambda i: None)  # no connection to simspark
    def test(self):
        from set_joint_commands import MyAgent

        perception = MagicMock()

        agent = MyAgent()
        action = agent.think(perception)

        self.assertEqual(action.stiffness['LShoulderPitch'], 0)
        self.assertEqual(action.speed['HeadYaw'], 0.1)


if __name__ == '__main__':
    unittest.main()
