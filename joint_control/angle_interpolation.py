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
from keyframes import hello
from keyframes import leftBellyToStand


class AngleInterpolationAgent(PIDAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(AngleInterpolationAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        self.keyframes = ([], [], [])

    def think(self, perception):
        target_joints = self.angle_interpolation(self.keyframes)
        self.target_joints.update(target_joints)
        return super(AngleInterpolationAgent, self).think(perception)

    def angle_interpolation(self, keyframes):
        target_joints = {}
        
        currentTime = self.perception.time
        names, times, keys = keyframes
        
        for i in range(len(names)): #iterate through all joints
            name = names[i]
            if name in self.joint_names: #only update known joints
                for j in range(len(times[i])-1): # each line of keys corresponds to a time
                   # if times[j] < currentTime < times[j+1]: #check which time we need to consider
                    angleOfJoint = keys[i][j][0]
                    handle2OfJoint = keys[i][j][2]
                    
                    delta_t0 = keys[i][j][1][1] # point 0
                    delta_angle0 = keys[i][j][1][2]
                    angle0 = self.calculateJointAngle(name, delta_angle0)
                    
                    delta_t1 = keys[i][j][2][1] #point 1
                    delta_angle1 = keys[i][j][2][2]
                    angle1 = self.calculateJointAngle(name, delta_angle1)
                    
                    delta_t2 = keys[i][j+1][1][1] #point 2
                    delta_angle2 = keys[i][j+1][1][2]
                    angle2 = self.calculateJointAngle(name, delta_angle2)
                    
                    delta_t3 = keys[i][j+1][2][1] #point 3
                    delta_angle3 = keys[i][j+1][2][2]
                    angle3 = self.calculateJointAngle(name, delta_angle3)
                    
                    c1 = (1-currentTime)**3
                    c2 = 3*(1-currentTime)**2
                    
                    target_joints[name] = c1*angle0 + c2*angle1*currentTime + c2*angle2*currentTime**2 + angle3*currentTime**3 #each joint will get a new angle value
        
        return target_joints
        
    def calculateJointAngle(self, jointName, delta_angle):
        return  self.perception.joint[jointName] + delta_angle
        

if __name__ == '__main__':
    agent = AngleInterpolationAgent()
    agent.keyframes = hello()  #hello, leftBackToStand, leftBellyToStand, rightBackToStand, rightBellyToStand, wipe_forehead
    agent.run()
    

