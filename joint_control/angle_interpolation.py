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
from keyframes import wipe_forehead
from keyframes import leftBackToStand
from keyframes import leftBellyToStand
from keyframes import rightBackToStand
from keyframes import rightBellyToStand
import numpy as np 

class AngleInterpolationAgent(PIDAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(AngleInterpolationAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        self.start = -1
        self.keyframes = ([], [], [])

    def think(self, perception):
        target_joints = self.angle_interpolation(self.keyframes, perception)
        self.target_joints.update(target_joints)
        return super(AngleInterpolationAgent, self).think(perception)

    def angle_interpolation(self, keyframes, perception):
        target_joints = {}
        # YOUR CODE HERE
    
        # Error checking 
        if(keyframes == ([],[],[])):
            #print('-Angle Interoplation-*** Error: emtpy keyframe ***')
            return target_joints
        else:
            (names, times, keys) = keyframes
        
        # for the first case   
        if (self.start == -1): 
            self.start = perception.time   
        
        # calculate time 
        timeInterval = perception.time - self.start 
        endIndex = 0
        
        # Iterate over all joint names
        for (jointNameIterator, name) in enumerate(names):
            timeSlot = times[jointNameIterator]
            UpperThresholdKeyF = 0 
            LowerThresholdKeyF = 0
            skippedJoints = 0
            
            #skip if outside of timeframe
            if timeSlot[-1] < timeInterval:
                skippedJoints += 1
                # if we skipped all joints then interpolation is done 
                # reset timer and keyframes
                if(skippedJoints == len(names)):
                    self.start = -1
                    self.keyframes = ([],[],[])
                continue
         
            # iterate over all times of the current joint to find the right time span 
            for timeIterator in range(len(times[jointNameIterator])):
                UpperThresholdKeyF = timeSlot[timeIterator]
                if (LowerThresholdKeyF <= timeInterval and UpperThresholdKeyF > timeInterval):
                        endIndex = timeIterator
                        break    
                LowerThresholdKeyF = UpperThresholdKeyF
            
            # calculate t-value
            t = 1 if (UpperThresholdKeyF - LowerThresholdKeyF) == 0. else (timeInterval - LowerThresholdKeyF) / (UpperThresholdKeyF - LowerThresholdKeyF)
            t = 1 if t > 1. else 0 if t < 0. else t 
            
            # Points
            if (endIndex != 0):
                p0 = keys[jointNameIterator][endIndex-1][0]
                p3 = keys[jointNameIterator][endIndex][0]
                p1 = p0 + keys[jointNameIterator][endIndex-1][1][2]
                p2 = p3 + keys[jointNameIterator][endIndex][1][2]
            elif (endIndex == 0):
                p0 = 0
                p1 = 0
                p3 = keys[jointNameIterator][0][0]
                p2 = p3 + keys[jointNameIterator][0][1][2]
                
            # bezier
            angle = ((1-t)**3)*p0 + 3*t*((1-t)**2)*p1 + 3*(t**2)*(1-t)*p2 + (t**3)*p3
            
            # Error correction due to simulation 
            if(name == "LHipYawPitch"):
                target_joints["RHipYawPitch"] = angle

            target_joints[name] = angle

        return target_joints

if __name__ == '__main__':
    agent = AngleInterpolationAgent()
    agent.keyframes = hello()  # CHANGE DIFFERENT KEYFRAMES
    agent.run()
