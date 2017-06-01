'''In this exercise you need to implement an angle interploation function which makes NAO executes keyframe motion

* Tasks:
    1. complete the code in `AngleInterpolationAgent.angle_interpolation`,
       you are free to use splines interploation or Bezier interploation,
       but the keyframes provided are for Bezier curves, you can simply ignore some data for splines interploation,
       please refer data format below for details.
    2. try different keyframes from `keyframes` folder

* Keyframe data format:
    keyframe := (names, times, keys)
    names := [str, ...]  # list of joint names
    times := [[float, float, ...], [float, float, ...], ...]
    # times is a matrix of floats: Each line corresponding to a joint, and column element to a key.
    keys := [[float, [int, float, float], [int, float, float]], ...]
    # keys is a list of angles in radians or an array of arrays each containing [float angle, Handle1, Handle2],
    # where Handle is [int InterpolationType, float dTime, float dAngle] describing the handle offsets relative
    # to the angle and time of the point. The first Bezier param describes the handle that controls the curve
    # preceding the point, the second describes the curve following the point.
'''


from pid import PIDAgent
from keyframes import leftBellyToStand #hello


class AngleInterpolationAgent(PIDAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(AngleInterpolationAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        self.keyframes = ([], [], [])
	self.start_time = self.perception.time

    def think(self, perception):
        target_joints = self.angle_interpolation(self.keyframes, perception)
        self.target_joints.update(target_joints)
        return super(AngleInterpolationAgent, self).think(perception)

    def angle_interpolation(self, keyframes, perception):
        target_joints = {}
        # YOUR CODE HERE
        
        current_time = perception.time - self.start_time
        
        (names, times, keys) = keyframes
        
	
	for i_joint in range(len(names)):
		name = names[i_joint]

		if name in self.joint_names: #only if the joint is known
			for i_time in range(len(times[i_joint]) - 1):

				#before the first viapoint
				if current_time < times[i_joint][0]:
                                        p0 = (0. , self.perception.joint[name])
					p3 = (times[i_joint][0] , keys[i_joint][0][0])
					p1 = ( p3[0] + keys[i_joint][0][1][1], p3[1] + keys[i_joint][0][1][2])
					p2 = p1 #we take the first handle of the first point as the second handle of the begin point
					t = current_time / p3[0]
					target_joints[name] = ((1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1])

				#between viapoints
				elif (times[i_joint][i_time] < current_time < times[i_joint][i_time + 1]):

					p0 = (times[i_joint][i_time] , keys[i_joint][i_time][0])
					p3 = (times[i_joint][i_time + 1] , keys[i_joint][i_time + 1][0])
					p1 = (p0[0] + keys[i_joint][i_time][2][1], p0[1] + keys[i_joint][i_time][2][2])
					p2 = (p3[0] + keys[i_joint][i_time][1][1], p3[1] + keys[i_joint][i_time][1][2])
					t = (current_time - p0[0]) / (p3[0] - p0[0])
					target_joints[name] = ((1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1])

			
        return target_joints



if __name__ == '__main__':
    agent = AngleInterpolationAgent()
    agent.keyframes = leftBellyToStand()#hello()  # CHANGE DIFFERENT KEYFRAMES
    agent.run()
