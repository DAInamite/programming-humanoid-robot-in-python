'''
In this exercise you need to know how to set joint commands.

* Tasks:
    1. set stiffness of LShoulderPitch to 0
    2. set speed of HeadYaw to 0.1

* Hint: The commands are store in action (class Action in spark_agent.py)

'''

# add PYTHONPATH
import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'software_installation'))

from spark_agent import SparkAgent


class MyAgent(SparkAgent):
    def think(self, perception):
        action = super(MyAgent, self).think(perception)
        # YOUR CODE HERE
        print("Setting joint commands stifness,speed")
        action.speed['HeadYaw'] = 0.1   #HeadYaw in Joint_CMD_NAMES
        action.stiffness['LShoulderPitch'] = 0  #LShoulderPitch in Joint_CMD_NAMES
        return action

if '__main__' == __name__:
    agent = MyAgent()
    agent.run()
