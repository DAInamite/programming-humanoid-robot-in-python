ALMotion
########

:version: stand_up_arm_collision-98-g5070a26-dirty

Interactive proxy to ALModule

isStatsEnabled()
================




enableStats()
=============




stats()
=======




clearStats()
============




isTraceEnabled()
================




enableTrace()
=============




exit()
======
Exits and unregisters the module.



pCall()
=======
NAOqi1 pCall method.



version()
=========
Returns the version of the module.


Returns
-------
A string containing the version of the module.

ping()
======
Just a ping. Always returns true


Returns
-------
returns true

getMethodList()
===============
Retrieves the module's method list.


Returns
-------
An array of method names.

getMethodHelp(methodName)
=========================
Retrieves a method's description.

Parameters
----------
:methodName: The name of the method.

Returns
-------
A structure containing the method's description.

getModuleHelp()
===============
Retrieves the module's description.


Returns
-------
A structure describing the module.

wait(id, timeoutPeriod)
=======================
Wait for the end of a long running method that was called using 'post'

Parameters
----------
:id: The ID of the method that was returned when calling the method using 'post'
:timeoutPeriod: The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero.

Returns
-------
True if the timeout period terminated. False if the method returned.

isRunning(id)
=============
Returns true if the method is currently running.

Parameters
----------
:id: The ID of the method that was returned when calling the method using 'post'

Returns
-------
True if the method is currently running

stop(id)
========
returns true if the method is currently running

Parameters
----------
:id: the ID of the method to wait for


getBrokerName()
===============
Gets the name of the parent broker.


Returns
-------
The name of the parent broker.

getUsage(name)
==============
Gets the method usage string. This summarises how to use the method.

Parameters
----------
:name: The name of the method.

Returns
-------
A string that summarises the usage of the method.

getStiffnesses(names)
=====================
Gets stiffness of a joint or group of joints.

Parameters
----------
:names: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'

Returns
-------
One or more stiffnesses. 1.0 indicates maximum stiffness. 0.0 indicated minimum stiffness

setStiffnesses(names, stiffnesses)
==================================
Sets the stiffness of one or more joints. This is a non-blocking call.

Parameters
----------
:names: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'
:stiffnesses: One or more stiffnesses between zero and one.


stiffnessInterpolation(names, stiffnesses, timeLists)
=====================================================
Interpolates one or multiple joints to a targeted stiffness or along timed trajectories of stiffness. This is a blocking call.

Parameters
----------
:names: Name or names of joints, chains, 'Body', 'BodyJoints' or 'BodyActuators'.
:stiffnesses: An stiffness, list of stiffnesses or list of list of stiffnesses.
:timeLists: A time, list of times or list of list of times.


wakeUp()
========
The robot wakes up: sets the Stiffness on and keeps is current position.



robotIsWakeUp()
===============
return true if the robot is already wakeUp


Returns
-------
True if the robot is already wakeUp.

angleInterpolation(names, angleLists, timeLists, isAbsolute)
============================================================
Interpolates one or multiple joints to a target angle or along timed trajectories. This is a blocking call.

Parameters
----------
:names: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'
:angleLists: An angle, list of angles or list of list of angles in radians
:timeLists: A time, list of times or list of list of times in seconds
:isAbsolute: If true, the movement is described in absolute angles, else the angles are relative to the current angle.


angleInterpolationWithSpeed(names, angleLists, maxSpeedFraction)
================================================================
Interpolates one or multiple joints to a target angle, using a fraction of max speed. Only one target angle is allowed for each joint. This is a blocking call.

Parameters
----------
:names: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'
:angleLists: An angle, or list of angles in radians
:maxSpeedFraction: A fraction.


angleInterpolationBezier(jointNames, times, controlPoints)
==========================================================
Interpolates a sequence of timed angles for several motors using bezier control points. This is a blocking call.

Parameters
----------
:jointNames: A vector of joint names
:times: An ragged ALValue matrix of floats. Each line corresponding to a motor, and column element to a control point.
:controlPoints: An ALValue array of arrays each containing [float angle, Handle1, Handle2], where Handle is [int InterpolationType, float dAngle, float dTime] descibing the handle offsets relative to the angle and time of the point. The first bezier param describes the handle that controls the curve preceeding the point, the second describes the curve following the point.


setAngles(names, angles, fractionMaxSpeed)
==========================================
Sets Angles. This is a non-blocking call.

Parameters
----------
:names: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'
:angles: One or more angles in radians
:fractionMaxSpeed: The fraction of maximum speed to use.


changeAngles(names, changes, fractionMaxSpeed)
==============================================
Changes Angles. This is a non-blocking call.

Parameters
----------
:names: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'
:changes: One or more changes in radians
:fractionMaxSpeed: The fraction of maximum speed to use.


changeHeadAngles(yaw, pitch, fractionMaxSpeed)
==============================================
Changes Angles of head. This is a non-blocking call.

Parameters
----------
:yaw: target angle of head yaw
:pitch: target angle of head pitch
:fractionMaxSpeed: The fraction of maximum speed to use.


getAngles(names, useSensors)
============================
Gets the angles of the joints.

Parameters
----------
:names: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'
:useSensors: If true, sensor angles will be returned

Returns
-------
Joint angles in radians.

closeHand(handName)
===================
NAO stiffens the motors of desired hand. Then, he closes the hand, then cuts motor current to conserve energy. This is a blocking call.

Parameters
----------
:handName: The name of the hand. Could be: "RHand" or "LHand"


openHand(handName)
==================
NAO stiffens the motors of desired hand. Then, he opens the hand, then cuts motor current to conserve energy. This is a blocking call.

Parameters
----------
:handName: The name of the hand. Could be: "RHand" or "LHand"


killMove()
==========
emergency Stop on Walk task: This method will end the walk task brutally, without attempting to return to a balanced state. If Nao has one foot in the air, he could easily fall.



moveInit()
==========
Initializes the walk process. Checks the robot pose and takes a right posture. This is blocking called.



setFootSteps(legName, footSteps, timeList, clearExisting)
=========================================================
Makes NAO do foot step planner. This is a non-blocking call.

Parameters
----------
:legName: name of the leg to move('LLeg' or 'RLeg'')
:footSteps: [x, y, theta], [Position along X/Y, Orientation round Z axis] of the leg relative to the other Leg in [meters, meters, radians]. Must be less than [MaxStepX, MaxStepY, MaxStepTheta]
:timeList: time list of each foot step
:clearExisting: Clear existing foot steps.


setFootStepsWithSpeed(legName, footSteps, fractionMaxSpeed, clearExisting)
==========================================================================
Makes NAO do foot step planner with speed. This is a non-blocking call.

Parameters
----------
:legName: name of the leg to move('LLeg' or 'RLeg')
:footSteps: [x, y, theta], [Position along X/Y, Orientation round Z axis] of the leg relative to the other Leg in [meters, meters, radians]. Must be less than [MaxStepX, MaxStepY, MaxStepTheta]
:fractionMaxSpeed: speed of each foot step. Must be between 0 and 1.
:clearExisting: Clear existing foot steps.


setFootTrajectory(legName, poseList, timeList, clearExisting)
=============================================================
set whole foot trajectory of one foot step. This is a non-blocking call.

Parameters
----------
:legName: name of the leg to move('LLeg' or 'RLeg')
:poseList: the path of foot in list of Vector6 [x, y, z, wx, wy, wz]
:timeList: time list of each pose
:clearExisting: Clear existing foot steps.


moveToward(x, y, theta, frequency)
==================================
Makes the robot move at the given normalized velocity, expressed in FRAME_ROBOT. This is a non-blocking call.

Parameters
----------
:x: normalized, unitless, velocity along X-axis. +1 and -1 correspond to the maximum velocity in the forward and backward directions, respectively.
:y: normalized, unitless, velocity along Y-axis. +1 and -1 correspond to the maximum velocity in the left and right directions, respectively.
:theta: normalized, unitless, velocity around Z-axis. +1 and -1 correspond to the maximum velocity in the counterclockwise and clockwise directions, respectively.
:frequency: Fraction of MaxStepFrequency [0.0 to 1.0]


move(x, y, theta)
=================
Makes the robot move at the given velocity, expressed in FRAME_ROBOT. This is a non-blocking call.

Parameters
----------
:x: velocity along X-axis, in meters per second. Use negative values for backward motion
:y: velocity along Y-axis, in meters per second. Use positive values to go to the left
:theta: velocity around Z-axis, in radians per second. Use negative values to turn clockwise.


setWalkTarget(x, y, theta)
==========================
Makes NAO walk to the given relative Position. This is a non-blocking call.

Parameters
----------
:x: Distance along the X axis in meters.
:y: Distance along the Y axis in meters.
:theta: Rotation around the Z axis in radians [-3.1415 to 3.1415].


moveTo(x, y, theta)
===================
Makes NAO walk to the given relative Position. This is a blocking call.

Parameters
----------
:x: Distance along the X axis in meters.
:y: Distance along the Y axis in meters.
:theta: Rotation around the Z axis in radians [-3.1415 to 3.1415].


getFootSteps()
==============
Get the actual foot steps vector. This is a non-blocking call.


Returns
-------
Each move of foot step is relative to the previous location of the opposite foot step. For example, a foot step move of LFoot will be relative to the last position of the RFoot.

getRobotPosition(useSensors)
============================
Gets the World Absolute Robot Position.

Parameters
----------
:useSensors: If true, use the MRE sensor values.

Returns
-------
(Absolute Position X, Absolute Position Y, Absolute Angle Theta (Wz)).

getNextRobotPosition(useSensors)
================================
Gets the World Absolute next Robot Position. When no walk process active, getNextRobotPosition() = getRobotPosition(). Else getNextRobotPosition return the position of the robot after the unchangeable foot steps.

Parameters
----------
:useSensors: If true, use the MRE sensor values.

Returns
-------
A vector containing the World Absolute next Robot position.(Absolute Position X, Absolute Position Y, Absolute Angle Theta (Wz))

getNextRobotPositionInRobotFrame()
==================================
Gets the next Robot Position in current robot frame. When no walk process active, it returns [0, 0, 0]


Returns
-------
A vector containing the next Robot position in current robot frame.

getRobotVelocity(useSensors)
============================
Gets the World Absolute Robot Velocity.

Parameters
----------
:useSensors: If true, use the sensor values.

Returns
-------
A vector containing the World Absolute Robot Velocity. (Absolute Velocity Translation X [m.s-1], Absolute Velocity Translation Y[m.s-1], Absolute Velocity Rotation WZ [rd.s-1])

moveIsActive()
==============
if Walk is Active.


Returns
-------
True if Walk is Active.

waitUntilMoveIsFinished()
=========================
this method can be used to block your script/code execution until the walk task is totally finished.



stopMove()
==========
Stops Walk task at next double support.



getMoveConfig(config)
=====================
Gets the foot Gait config ("MaxStepX", "MaxStepY", "MaxStepTheta",  "MaxStepFrequency", "StepHeight", "TorsoWx", "TorsoWy")

Parameters
----------
:config: a string should be "Max", "Min", "Default"

Returns
-------
An ALvalue with the following form :[["MaxStepX", value], ["MaxStepY", value], ["MaxStepTheta", value], ["MaxStepFrequency", value], ["StepHeight", value], ["TorsoWx", value], ["TorsoWy", value]]

setWalkArmsEnabled(leftArmEnable, rightArmEnable)
=================================================
Sets if Arms Motions are enabled during the Walk Process.

Parameters
----------
:leftArmEnable: if true Left Arm motions are controlled by the Walk Task
:rightArmEnable: if true Right Arm mMotions are controlled by the Walk Task


getWalkArmsEnabled()
====================
Gets if Arms Motions are enabled during the Walk Process.


Returns
-------
True Arm Motions are controlled by the Walk Task.

getWalkStatistics()
===================
Gets statistics of walk.


Returns
-------
statistics of walk in string

wereFeetCollidedDuringMoving()
==============================
Gets the collided status of feet's bumper


Returns
-------
if collision happened for left foot and right foot during last move

setStopMoveWhenFootCollidedEnabled(bool)
========================================
stop move when foot collided during move.

Parameters
----------
:bool: enable or not


getStopMoveWhenFootCollidedEnabled()
====================================
get if stopping move when foot collided during move.


Returns
-------
enabled or not

requestMoveEmergencyStop()
==========================
request stopping move as soon as possible.



getFootGaitConfig()
===================
Deprecated, use getMoveConfig instead.



getWalkArmsEnable()
===================
Deprecated, use getWalkArmsEnabled instead.



setWalkArmsEnable()
===================
Deprecated, use setWalkArmsEnabled instead.



killWalk()
==========
Deprecated, use killMove instead.



stopWalk()
==========
Deprecated, use stopMove instead.



waitUntilWalkIsFinished()
=========================
Deprecated, use waitUntilMoveIsFinished instead.



walkInit()
==========
Deprecated, use moveInit instead.



walkIsActive()
==============
Deprecated, use moveIsActive instead.



walkTo()
========
Deprecated, use moveTo instead.



getTransform(name, space, useSensorValues)
==========================================
Gets an Homogenous Transform relative to the TASK_SPACE. Axis definition: the x axis is positive toward NAO's front, the y from right to left and the z is vertical.

Parameters
----------
:name: Name of the item. Could be: any joint or chain or sensor (Head, LArm, RArm, LLeg, RLeg, Torso, HeadYaw, ..., CameraTop, CameraBottom, MicroFront, MicroRear, MicroLeft, MicroRight, Accelerometer, Gyrometer, Laser, LFsrFR, LFsrFL, LFsrRR, LFsrRL, RFsrFR, RFsrFL, RFsrRR, RFsrRL, USSensor1, USSensor2, USSensor3, USSensor4. Use getSensorNames for the list of sensors supported on your robot.
:space: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:useSensorValues: If true, the sensor values will be used to determine the position.

Returns
-------
corresponding to the values of the matrix, line by line.

getTransforms(names, frame, useSensorValues)
============================================
Gets an Homogenous Transforms relative to the frame. The return values are consistency, so the function will take one motion until return.

Parameters
----------
:names: Names of the items.
:frame: Task frame
:useSensorValues: If true, the sensor values will be used to determine the position.

Returns
-------
corresponding to the values of the matrix, line by line.

setTransform(chainName, space, transform, fractionMaxSpeed, axisMask)
=====================================================================
Moves an end-effector to the given position and orientation transform. This is a non-blocking call.

Parameters
----------
:chainName: Name of the chain. Could be: 'Head', 'LArm','RArm', 'LLeg', 'RLeg', 'Torso'
:space: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:transform: Transform arrays
:fractionMaxSpeed: The fraction of maximum speed to use
:axisMask: Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both


changeTransform(chainName, space, transform, fractionMaxSpeed, axisMask)
========================================================================
Moves an end-effector to the given position and orientation transform. This is a non-blocking call.

Parameters
----------
:chainName: Name of the chain. Could be: 'Head', 'LArm','RArm', 'LLeg', 'RLeg', 'Torso'
:space: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:transform: Transform arrays
:fractionMaxSpeed: The fraction of maximum speed to use
:axisMask: Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both


getPosition(name, space, useSensorValues)
=========================================
Gets a Position relative to the TASK_SPACE. Axis definition: the x axis is positive toward NAO's front, the y from right to left and the z is vertical. The angle convention of Position6D is Rot_z(wz).Rot_y(wy).Rot_x(wx).

Parameters
----------
:name: Name of the item. Could be: any joint or chain or sensor (Head, LArm, RArm, LLeg, RLeg, Torso, HeadYaw, ..., CameraTop, CameraBottom, MicroFront, MicroRear, MicroLeft, MicroRight, Accelerometer, Gyrometer, Laser, LFsrFR, LFsrFL, LFsrRR, LFsrRL, RFsrFR, RFsrFL, RFsrRR, RFsrRL, USSensor1, USSensor2, USSensor3, USSensor4. Use getSensorNames for the list of sensors supported on your robot.
:space: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:useSensorValues: If true, the sensor values will be used to determine the position.

Returns
-------
corresponding to the values of the matrix, line by line.

setPosition(chainName, space, position, fractionMaxSpeed, axisMask)
===================================================================
Moves an end-effector to the given position and orientation. This is a non-blocking call.

Parameters
----------
:chainName: Name of the chain. Could be: 'Head', 'LArm','RArm', 'LLeg', 'RLeg', 'Torso'
:space: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:position: 6D position array (x,y,z,wx,wy,wz) in meters and radians
:fractionMaxSpeed: The fraction of maximum speed to use
:axisMask: Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both


changePosition(chainName, space, positionChange, fractionMaxSpeed, axisMask)
============================================================================
Creates a move of an end effector in cartesian space. This is a non-blocking call.

Parameters
----------
:chainName: Name of the chain. Could be: 'Head', 'LArm','RArm', 'LLeg', 'RLeg', 'Torso'
:space: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:positionChange: 6D position array (x,y,z,wx,wy,wz) in meters and radians
:fractionMaxSpeed: The fraction of maximum speed to use
:axisMask: Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both


positionInterpolation(chainName, space, path, axisMask, duration, isAbsolute)
=============================================================================
Moves an end-effector to the given position and orientation over time. This is a blocking call.

Parameters
----------
:chainName: Name of the chain. Could be: 'Head', 'LArm','RArm', 'LLeg', 'RLeg', 'Torso'
:space: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:path: Vector of 6D position arrays (x,y,z,wx,wy,wz) in meters and radians
:axisMask: Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both
:duration: Vector of times in seconds corresponding to the path points
:isAbsolute: If true, the movement is absolute else relative


positionInterpolations(chainName, taskSpaceForAllPaths, path, axisMask, relativeTimes, isAbsolute)
==================================================================================================
Moves end-effector to the given transforms over time. This is a blocking call.

Parameters
----------
:chainName: Name of the chain. Could be: 'Head', 'LArm','RArm', 'LLeg', 'RLeg', 'Torso'
:taskSpaceForAllPaths: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:path: Vector of 6D position arrays (x,y,z,wx,wy,wz) in meters and radians
:axisMask: Vector of Axis Masks. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both
:relativeTimes: Vector of times in seconds corresponding to the path points
:isAbsolute: If true, the movement is absolute else relative


transformInterpolation(chainName, space, path, axisMask, duration, isAbsolute)
==============================================================================
Moves an end-effector to the given position and orientation over time using homogenous transforms to describe the positions or changes. This is a blocking call.

Parameters
----------
:chainName: Name of the chain. Could be: 'Head', 'LArm','RArm', 'LLeg', 'RLeg', 'Torso'
:space: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:path: Vector of Transform arrays
:axisMask: Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both
:duration: Vector of times in seconds corresponding to the path points
:isAbsolute: If true, the movement is absolute else relative


transformInterpolations(chainName, taskSpaceForAllPaths, path, axisMask, relativeTimes, isAbsolute)
===================================================================================================
Moves end-effector to the given transforms over time. This is a blocking call.

Parameters
----------
:chainName: Name of the chain. Could be: 'Head', 'LArm','RArm', 'LLeg', 'RLeg', 'Torso'
:taskSpaceForAllPaths: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}.
:path: Vector of Transform arrays
:axisMask: Vector of Axis Masks. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both
:relativeTimes: Vector of times in seconds corresponding to the path points
:isAbsolute: If true, the movement is absolute else relative


getCameraMatrix(cameraId, sec, usec)
====================================
get camera matrix by given time

Parameters
----------
:cameraId: 0 for CameraTop, 1 for CameraBottom.
:sec: time in seconds.
:usec: time in microseconds.

Returns
-------
corresponding to the values of the matrix, line by line.

wbEnable()
==========
Not implemented.



wbEnableBalanceConstraint()
===========================
Not implemented.



wbEnableEffectorControl()
=========================
Not implemented.



wbEnableEffectorOptimization()
==============================
Not implemented.



wbFootState()
=============
Not implemented.



wbGoToBalance()
===============
Not implemented.



wbSetEffectorControl()
======================
Not implemented.



setCollisionProtectionEnabled(pChainName, pEnable)
==================================================
Enable Anticollision protection of the arms of the robot. Use api isCollision to know if a chain is in collision and can be disactivated.

Parameters
----------
:pChainName: The chain name {"Arms", "LArm" or "RArm"}.
:pEnable: Activate or disactivate the anticollision of the desired Chain.

Returns
-------
True if the value is set successfully

getCollisionProtectionEnabled(pChainName)
=========================================
Allow to know if the collision protection is activated on the given chain.

Parameters
----------
:pChainName: The chain name {"LArm" or "RArm"}.

Returns
-------
Return true is the collision protection of the given Arm is activated.

isCollision(pChainName)
=======================
Give the collision state of a chain. If a chain has a collision state "none" or "near", it could be desactivated.

Parameters
----------
:pChainName: The chain name {"Arms", "LArm" or "RArm"}.

Returns
-------
A string which notice the collision state: "none" there are no collision, "near" the collision is taking in account in the anti-collision algorithm, "collision" the chain is in contact with an other body. If the chain asked is "Arms" the most unfavorable result is given.

getColliders(useSensors)
========================
get colliders which are used for self collision avoidance

Parameters
----------
:useSensors: If ture, colliders from sensor model are returned

Returns
-------
each collider contains type and data

getCollisionBetweenColliders(collider, collidee, useSensors)
============================================================
get closest points of two colliders

Parameters
----------
:collider: name of first collider
:collidee: name of second collider
:useSensors: If ture, colliders from sensor model are used

Returns
-------
points from two colliders

getClosestCollider(collider, useSensors)
========================================
get closest collider of given collider

Parameters
----------
:collider: name of collider
:useSensors: If ture, colliders from sensor model are used

Returns
-------
name of the closest collider

getMinDistanceToColliders(p0, p1, useSensors)
=============================================
get minimum distance between given segment and all colliders

Parameters
----------
:p0: first point of segment
:p1: second point of segment
:useSensors: If ture, colliders from sensor model are used

Returns
-------
minimum distance between given segment and all colliders

checkSightBlocking(posInFrameRobot, id, sec, usec)
==================================================
check if positions are blocked by body in the view sight

Parameters
----------
:posInFrameRobot: lost of positions in FRAME_ROBOT
:id: the id of camera
:sec: time in seconds.
:usec: time in microseconds.

Returns
-------
minimum distances between line of sight and bodies, positive value means no blocking, and negative value means blocking

getCameraMatrixWithBodyContour(cameraId, sec, usec)
===================================================
get camera matrix and body contour

Parameters
----------
:cameraId: the id of camera
:sec: time in seconds.
:usec: time in microseconds.

Returns
-------
camera matrix and vector of contour lines (vector of Vector3)

getLeftArmPushing()
===================
get extenal 'force' applied to left arm


Returns
-------
x, y direction of pushing

getRightArmPushing()
====================
get extenal 'force' applied to right arm


Returns
-------
x, y direction of pushing

isCoMInsideSupportPolygon()
===========================
Returns true if center of mass is inside support polygon


Returns
-------
if center of mass is inside support polygon

getJointNames()
===============
Deprecated, use getBodyNames instead.



getBodyNames(name)
==================
Gets the names of all the joints in the collection.

Parameters
----------
:name: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'

Returns
-------
one for each joint in the collection

getSensorNames()
================
Gets the list of sensors supported on your robot.


Returns
-------
Vector of sensor names

getLimits(name)
===============
Get the minAngle (rad), maxAngle (rad), and maxVelocity (rad.s-1) for a given joint or actuator in the body.

Parameters
----------
:name: Name of a joint, chain, 'Body', 'BodyJoints' or 'BodyActuators'.

Returns
-------
Array of ALValue arrays containing the minAngle, maxAngle, maxVelocity and maxTorque for all the joints specified.

getRobotConfig()
================
Get the robot configuration.


Returns
-------
containing the robot parameter names and the robot parameter values.

getSummary()
============
Returns a string representation of the Model's state.


Returns
-------
A formated string

getMass(pName)
==============
Gets the mass of a joint, chain, 'Body' or 'BodyJoints'.

Parameters
----------
:pName: Name of the body which we want the mass. 'Body' and 'BodyJoints' give the total mass of NAO. For the chain, it gives the total mass of the chain.

Returns
-------
The mass in kg.

getCOM(pName, pSpace, pUseSensorValues)
=======================================
Gets the COM of a joint, chain, 'Body' or 'BodyJoints'.

Parameters
----------
:pName: Name of the body which we want the mass. In chain name case, this function give the com of the chain.
:pSpace: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}
:pUseSensorValues: If true, the sensor values will be used to determine the position.

Returns
-------
The COM position (meter).

getCenterOfPressure(pSpace)
===========================
Gets the center of pressure.

Parameters
----------
:pSpace: Task space {SPACE_TORSO = 0, SPACE_WORLD = 1, SPACE_NAO = 2}

Returns
-------
The center of pressure position (meter), empty list when it is invalid.

setMotionConfig(config)
=======================
set parameters of motion.

Parameters
----------
:config: An array of ALValues [i][0]: name, [i][1]: value


setConfig(config)
=================
set parameters of motion.

Parameters
----------
:config: An array of ALValues [i][0]: name, [i][1]: value


getMotionConfig(key)
====================
get configuation of motion

Parameters
----------
:key: string


getConfig(key)
==============
get configuation of motion

Parameters
----------
:key: string


getMotionConfigAll()
====================
get all configuation of motion


Returns
-------
{name: value}

getAllConfig()
==============
get all configuation of motion


Returns
-------
{name: value}

saveMotionConfig()
==================
save parameters of motion.



saveConfig()
============
save parameters of motion.



getMotionCycleTime()
====================
Get the motion cycle time in milliseconds.


Returns
-------
the cycle time in milliseconds

updateTrackerTarget(pTargetPositionWy, pTargetPositionWz, pTimeSinceDetectionMs, pUseOfWholeBody)
=================================================================================================
Update the target to follow by the head of NAO. This function is mainly use by the tracker modules.

Parameters
----------
:pTargetPositionWy: The target position wy in SPACE_NAO
:pTargetPositionWz: The target position wz in  SPACE_NAO
:pTimeSinceDetectionMs: The time in Ms since the target was detected
:pUseOfWholeBody: If true, the target is follow in cartesian space by the Head with whole Body constraints.


getPosture()
============
get posture of robot


Returns
-------
name of current posture, e.g. Stand, Sit

setPostureConfig(cfg)
=====================
set configuration for posture detection

Parameters
----------
:cfg: string of configuration same as content of config file


rest()
======
The robot rests: goes to a relax and safe position and sets Motor off. For example, H25 or H21 goes to the Crouch posture and sets the Stiffness off.



setSmartStiffnessEnabled(pEnable)
=================================
Enable Smart Stiffness for all the joints (True by default), the update take one motion cycle for updating. The smart Stiffness is a gestion of joint maximum torque. More description is available on the red documentation of ALMotion module.

Parameters
----------
:pEnable: Activate or disactivate the smart stiffness.


getSmartStiffnessEnabled()
==========================
Give the state of the smart Stiffness.


Returns
-------
Return true is the smart Stiffnes is activated.

setFallManagerEnabled(pEnable)
==============================
Enable The fall manager protection for the robot. When a fall is detected the robot adopt a joint configuration to protect himself and cut the stiffness. An memory event called "robotHasFallen" is generated when the fallManager have been activated.

Parameters
----------
:pEnable: Activate or disactivate the smart stiffness.


getFallManagerEnabled()
=======================
Give the state of the fall manager.


Returns
-------
Return true is the fall manager is activated.

getTemperature(names)
=====================
Gets the temperature of the joints.

Parameters
----------
:names: Name of a chain, 'Body', 'BodyJoints' or 'BodyActuators'

Returns
-------
temperature in deg Celsius

getIMUData()
============
get data from IMU filter


Returns
-------
[[angleX, speedX], [angleY, speedY]]

getClockTime()
==============
get current clock time of motion


Returns
-------
time in seconds and microseconds

getBatteryState()
=================
get state of battery


Returns
-------
[current, charge, temperature]

getButtonsPressed()
===================
get state of buttons, True for pressed


Returns
-------
[ChestButtonPressed, LeftBumperPressed, RightBumperPressed]

getTaskList()
=============
Gets an ALValue structure describing the tasks in the Task List


Returns
-------
An ALValue containing an ALValue for each task. The inner ALValue contains: Name, MotionID

getTaskLog()
============
Gets a list of task logs


Returns
-------
An vector of string which are logs of tasks

areResourcesAvailable(resourceNames)
====================================
Returns true if all the desired resources are available. Only motion API's' blocking call takes resources.

Parameters
----------
:resourceNames: An vector of resource names such as joints. Use getJointNames("Body") to have the list of the available joint for your robot.

Returns
-------
True if the resources are available

killTask(motionTaskID)
======================
Kills a motion task.

Parameters
----------
:motionTaskID: TaskID of the motion task you want to kill.

Returns
-------
Return true if the specified motionTaskId has been killed.

killTasksUsingResources(resourceNames)
======================================
Kills all tasks that use any of the resources given. Only motion API's' blocking call takes resources and can be killed. Use getJointNames("Body") to have the list of the available joint for your robot.

Parameters
----------
:resourceNames: An vector of resource joint names


stopTasksUsingResources(resourceNames)
======================================
stops all tasks that use any of the resources given. Use getJointNames("Body") to have the list of the available joint for your robot. This is a blocking call.

Parameters
----------
:resourceNames: An vector of resource joint names


killAll()
=========
Kills all tasks.



stopAll()
=========
stops all tasks.



getDescription()
================
get description message



test(cmd)
=========
test motion.

Parameters
----------
:cmd: [command [arguments]]


getSensorDataNames()
====================
get names of sensor data


Returns
-------
a list contains all the names of sensors

getSensorData()
===============
get sensor data in string


Returns
-------
sensor data

setLoggingDataCapacity(capacity)
================================
set the capacity buffer for logging sensor and actuator data. The logging is disabled when capacity is zero.

Parameters
----------
:capacity: size of capacity, 0 to disable logging


getLoggingDataCapacity()
========================
get the capacity buffer for logging sensor and actuator data.


Returns
-------
size of capacity, 0 means the logging is disabled

dumpLoggingData(filename)
=========================
save logging sensor and actuator data to files.

Parameters
----------
:filename: the filename for saving data


getLoggingData()
================
get logging sensor and actuator data


Returns
-------
[[[sensor_0],[sensor_1],...], [[actutor_0],[actuator_1],...]]

dumpMemory(filename)
====================
dump memory into file, which includes sensor, actuator and perception buffer

Parameters
----------
:filename: the filename for saving data


getMemoryDump()
===============
get memory dump as string


Returns
-------
binary data of memory dumpy

getSupportPolygon()
===================
get vertexes of support polygon in SPACE_NAO


Returns
-------
[[x0, y0], [x1, y1], ...]

getFeetTouch()
==============
get touch state of feet


Returns
-------
[leftFootTouch, rightFootTouch]

getTimeHistogram()
==================
get histogram of execuating time


Returns
-------
[[t0, n0], [t1, n1] ...]

checkActuator()
===============
check if the status of actuator is fine, an exception is raised when unnormal behavior is detected



calculateLegAnglesIK(torso, lFoot, rFoot)
=========================================
calculate angles of Legs with given poses of feet and torso

Parameters
----------
:torso: pose of torso (Vector6)
:lFoot: pose of left foot (Vector6)
:rFoot: pose of right foot (Vector6)

Returns
-------
[[joint1, angle1], [joint2, angle2], ...]

setPlotDataEnabled(name, Ture or False)
=======================================
enable/disable logging data for plots

Parameters
----------
:name: name of data
:Ture or False: enable or disable


setPlotBufferCapacity(capacity)
===============================
set capacity of data buffer for plotting

Parameters
----------
:capacity: size of capacity


getPlotData(names)
==================
get data for plots

Parameters
----------
:names: vector of names, e.g. ['a', 'b', ...]

Returns
-------
[[a0, a1, ...], [b0, b1, ...], ...]

getPlotDataList()
=================
get list of plots avaiable


Returns
-------
string and bool pair indicates that if the plot is enabled or not

findPlot(startStr)
==================
get list of plots avaiable

Parameters
----------
:startStr: the start string to find plot

Returns
-------
names of plot start with given string

modify(name, value)
===================
modify variables for debugging

Parameters
----------
:name: name of data
:value: value of data


removeModify(name)
==================
remove (disable) modifing variables

Parameters
----------
:name: name of data


setDrawingEnabled(enabled)
==========================
enable/disable drawing log

Parameters
----------
:enabled: bool


saveDrawingLog(filename)
========================
save drawing log to file

Parameters
----------
:filename: string


getBuildOptionWarnMessage()
===========================
get warning message when debugging option was enabled during build



dumpStatistics(string)
======================
dump statistics of motion to file

Parameters
----------
:string: file name


diagnosis()
===========
diagnosis sensors and joints of robot


Returns
-------
diagnosis result in text
