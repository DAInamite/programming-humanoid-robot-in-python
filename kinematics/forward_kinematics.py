'''In this exercise you need to implement forward kinematics for NAO robot

* Tasks:
    1. complete the kinematics chain definition (self.chains in class ForwardKinematicsAgent)
       The documentation from Aldebaran is here:
       http://doc.aldebaran.com/2-1/family/robots/bodyparts.html#effector-chain
    2. implement the calculation of local transformation for one joint in function
       ForwardKinematicsAgent.ans. The necessary documentation are:
       http://doc.aldebaran.com/2-1/family/nao_h21/joints_h21.html
       http://doc.aldebaran.com/2-1/family/nao_h21/links_h21.html
    3. complete function ForwardKinematicsAgent.forward_kinematics, save the transforms of all body parts in torso
       coordinate into self.transforms of class ForwardKinematicsAgent
* Hints:
    the local_trans has to consider different joint axes and link parameters for differnt joints
'''

# add PYTHONPATH
import os
import sys
import math
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'joint_control'))

from numpy.matlib import matrix, identity


from angle_interpolation import AngleInterpolationAgent


class ForwardKinematicsAgent(AngleInterpolationAgent):
	def __init__(self, simspark_ip='localhost',
		simspark_port=3100,
		teamname='DAInamite',
		player_id=0,
		sync_mode=True):
		super(ForwardKinematicsAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
		self.transforms = {n: identity(4) for n in self.joint_names}

		# chains defines the name of chain and joints of the chain
		self.chains = {'Head': ['HeadYaw', 'HeadPitch'],
				'LArm' : ['LShoulderPitch','LShoulderRoll','LElbowYaw','LElbowRoll'],
				'LLeg' : ['LHipYawPitch','LHipRoll','LHipPitch','LKneePitch','LAnklePitch','LAnkleRoll'],
				'RLeg' : ['RHipYawPitch','RHipRoll','RHipPitch','RKneePitch','RAnklePitch','RAnkleRoll'],
				'RArm' : ['RShoulderPitch','RShoulderRoll','RElbowYaw','RElbowRoll']
				}

	def think(self, perception):
		self.forward_kinematics(perception.joint)
		return super(ForwardKinematicsAgent, self).think(perception)

	def local_trans(self, joint_name, joint_angle):
		'''calculate local transformation of one joint

		:param str joint_name: the name of joint
		:param float joint_angle: the angle of joint in radians
		:return: transformation
		:rtype: 4x4 matrix
		'''
		T = matrix(0)
		s = math.sin(joint_angle)
		c = math.cos(joint_angle)
		'''print T, s, c'''
		print joint_name
		if 'Pitch' in joint_name :
			T = T +([[c,0,s,0],
				 [0,1,0,0],
				[-s,0,c,0],
				[0,0,0,1]])
			if "Shoulder" in joint_name :
				T = T + ([[0,0,0,0],
		  			[0,0,0,98],
					[0,0,0,100],
					[0,0,0,0]])

			if "Knee" in joint_name :
				T = T + ([[0,0,0,0],
		  			[0,0,0,0],
					[0,0,0,-102.9],
					[0,0,0,0]])
			if "Ankle" in joint_name :
				T = T + ([[0,0,0,0],
					[0,0,0,50],
					[0,0,0,-85],
					[0,0,0,0]])
		elif 'Yaw' in joint_name :
			T = T + ([[c,s,0,0],
				[-s,c,0,0],
				[0,0,0,0],
				[0,0,0,1]])
			if 'Head' in joint_name :
				T = T + ([[0,0,0,0],
					[0,0,0,0],
					[0,0,0,126.5],
					[0,0,0,0]])
			if "Elbow" in joint_name :
				T = T + ([[0,0,0,105],
					[0,0,0,15],
					[0,0,0,0],
					[0,0,0,0]])
			if "Wrist" in joint_name :
				T = T + ([[0,0,0,55.95],
					[0,0,0,0],
					[0,0,0,0],
					[0,0,0,0]])
			if "Hip" in joint_name :
				T = T + ([[0,0,0,0],
					[0,0,0,50],
					[0,0,0,-85],
					[0,0,0,0]])
		elif 'Roll' in joint_name :
				T = T + ([[1,0,0,0],
					[0,c,-s,0],
					[0,s,c,0],
					[0,0,0,1]])

		return T

	def forward_kinematics(self, joints):
		for chain_joints in self.chains.values():
			T = identity(4)

			for joint in chain_joints:
				angle = joints[joint]
				Tl = self.local_trans(joint, angle)

				# YOUR CODE HERE
				T = T * Tl
				self.transforms[joint] = T


if __name__ == '__main__':
    agent = ForwardKinematicsAgent()
    agent.run()
