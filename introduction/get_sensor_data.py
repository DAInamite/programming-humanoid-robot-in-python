'''
In this exercise you need to know how to get sensor data.

* Task: get the current joint angle and tempeture of joint HeadYaw

* Hit: The current sensor data of robot are store in perception (class Perception in spark_agent.py)

'''

from spark_agent import SparkAgent


class MyAgent(SparkAgent):
    def think(self, perception):
        angle = perception.joint.get('HeadYaw')
        tempeture = perception.joint_temperature.get('HeadYaw')
        
        # set angle and tempeture to current data of joint HeadYaw

        print 'HeadYaw angle: ' + str(angle) + ' tempeture: ' + str(tempeture)
        return super(MyAgent, self).think(perception)

if '__main__' == __name__:
    agent = MyAgent()
    agent.run()
