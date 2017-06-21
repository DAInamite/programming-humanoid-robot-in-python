'''In this exercise you need to implement inverse kinematics for NAO's legs
* Tasks:
    1. solve inverse kinematics for NAO's legs by using analytical or numerical method.
       You may need documentation of NAO's leg:
       http://doc.aldebaran.com/2-1/family/nao_h21/joints_h21.html
       http://doc.aldebaran.com/2-1/family/nao_h21/links_h21.html
    2. use the results of inverse kinematics to control NAO's legs (in InverseKinematicsAgent.set_transforms)
       and test your inverse kinematics implementation.
'''


from forward_kinematics import ForwardKinematicsAgent
from numpy.matlib import identity


class InverseKinematicsAgent(ForwardKinematicsAgent):
    def inverse_kinematics(self, effector_name, transform):
        '''solve the inverse kinematics
        :param str effector_name: name of end effector, e.g. LLeg, RLeg
        :param transform: 4x4 transform matrix
        :return: list of joint angles
        '''
        joint_angles = {}
        for chain in self.chains[effector_name]:
            joint_angles[chain] = joints[chain]

        error = 0
        error_limit = 1e-4
        lambda_ = 0.001
        theta=0
        target = self.from_trans(transform)
        chain_of_effector = self.chains[effector_name]

        while True:
            self.forward_kinematics(joint_angles)
            T = []
            for chain in self.chains:
                T.append(self.transforms[chain])

            Te = np.matrix([self.from_trans(T[-1])])
            e = target - Te
            T = np.matrix([self.from_trans(i) for i in T[0:-1]])
            J = Te - T
            J = J.T
            J[-1, :] = 1  # angular velocity
            JJT = np.dot(J, J.T)
            d_theta = lambda_ * J.T * JJT.I * e.T
            theta += np.asarray(d_theta.T)[0]

            i = 0
            for chain in self.chains:
                joint_angles[chain] += np.asarray(d_theta.T)[0][i]
                i +=1
            error = np.linalg.norm(d_theta)
            if error < error_limit:
                return joint_angles
        return joint_angles

    def set_transforms(self, effector_name, transform):
        '''solve the inverse kinematics and control joints use the results
        '''
        # YOUR CODE HERE
        joint_angles = self.inverse_kinematics(effector_name, transform)
        chain = self.chains[effector_name]
        self.keyframes = (chain, [[0, 1]] * len(chain), joint_angles)  # the result joint angles have to fill in
        return joint_angles
        
    def from_trans(self, m):
        theta_x, theta_y, theta_z = 0,0,0
        #x
        if m[0, 0] == 1:
            theta_x = np.arctan2(m[2, 1], m[1, 1])
        #y
        elif m[1, 1] == 1:
            theta_y = np.arctan2(m[0, 2], m[0, 0])
        #z
        elif m[2, 2] == 1:
            theta_z = np.arctan2(m[1, 0], m[0, 0])
        return np.array([m[3, 0], m[3, 1], m[3, 2], theta_x, theta_y, theta_z])

if __name__ == '__main__':
    agent = InverseKinematicsAgent()
    # test inverse kinematics
    T = identity(4)
    T[-1, 1] = 0.05
    T[-1, 2] = 0.26
    agent.set_transforms('LLeg', T)
agent.run()
