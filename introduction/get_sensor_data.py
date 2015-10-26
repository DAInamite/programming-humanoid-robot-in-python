'''
In this exercise you need to know how to get sensor data.

* Task: get the current joint angle and temperature of joint HeadYaw

* Hit: The current sensor data of robot are store in perception (class Perception in spark_agent.py)

'''

from spark_agent import SparkAgent


class MyAgent(SparkAgent):
    def think(self, perception):
        angle = 0
        temperature = 0
        # YOUR CODE HERE
        # set angle and temperature to current data of joint HeadYaw

        print 'HeadYaw angle: ' + str(angle) + ' temperature: ' + str(temperature)
        return super(MyAgent, self).think(perception)

if '__main__' == __name__:
    agent = MyAgent()
    agent.run()
