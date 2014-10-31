'''In this exercise you need to implement the PID controller for joints of robot.

* Task:
    1. complete the control function in PIDController
    2. adjust PID parameters for NAO in simulation
'''

# add PYTHONPATH
import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'introduction'))

import numpy as np
from spark_agent import SparkAgent, JOINT_CMD_NAMES


class PIDController(object):
    '''a discretized PID controller
    '''
    def __init__(self, dt, size):
        self.dt = dt
        self.u = np.zeros(size)
        self.e1 = np.zeros(size)
        self.e2 = np.zeros(size)
        # ADJUST PARAMETERS BELOW
        self.Kp = 0
        self.Ki = 0
        self.Kd = 0

    def control(self, e):
        '''apply PID control
        @param e: current tracking error
        @return control signal
        '''
        # YOUR CODE HERE
        a = self.Kp + self.Ki * self.dt + self.Kd / self.dt
        b = -(self.Kp + 2 * self.Kd / self.dt)
        c = self.Kd / self.dt
        self.u += (e * a + self.e1 * b + self.e2 * c)
        self.e2 = self.e1
        self.e1 = e
        return self.u


class PIDAgent(SparkAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(PIDAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        self.joint_names = JOINT_CMD_NAMES.keys()
        number_of_joints = len(self.joint_names)
        self.joint_controller = PIDController(dt=0.01, size=number_of_joints)
        self.target_joints = {k: 0 for k in self.joint_names}

    def think(self, perception):
        action = super(PIDAgent, self).think(perception)
        joint_angles = np.asarray(perception.joint.values())
        target_angles = np.asarray(self.target_joints.values())
        e = target_angles - joint_angles
        u = self.joint_controller.control(e)
        action.speed = dict(zip(self.joint_names, u))
        return action


if __name__ == '__main__':
    agent = PIDAgent()
    agent.target_joints['HeadYaw'] = 1.0
    agent.run()
