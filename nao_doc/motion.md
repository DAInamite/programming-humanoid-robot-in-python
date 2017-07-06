ALMotion
========

version  
stand\_up\_arm\_collision-98-g5070a26-dirty

Interactive proxy to ALModule

isStatsEnabled()
----------------

enableStats()
-------------

stats()
-------

clearStats()
------------

isTraceEnabled()
----------------

enableTrace()
-------------

exit()
------

Exits and unregisters the module.

pCall()
-------

NAOqi1 pCall method.

version()
---------

Returns the version of the module.

### Returns

A string containing the version of the module.

ping()
------

Just a ping. Always returns true

### Returns

returns true

getMethodList()
---------------

Retrieves the module’s method list.

### Returns

An array of method names.

getMethodHelp(methodName)
-------------------------

Retrieves a method’s description.

### Parameters

methodName  
The name of the method.

### Returns

A structure containing the method’s description.

getModuleHelp()
---------------

Retrieves the module’s description.

### Returns

A structure describing the module.

wait(id, timeoutPeriod)
-----------------------

Wait for the end of a long running method that was called using ‘post’

### Parameters

id  
The ID of the method that was returned when calling the method using ‘post’

timeoutPeriod  
The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero.

### Returns

True if the timeout period terminated. False if the method returned.

isRunning(id)
-------------

Returns true if the method is currently running.

### Parameters

id  
The ID of the method that was returned when calling the method using ‘post’

### Returns

True if the method is currently running

stop(id)
--------

returns true if the method is currently running

### Parameters

id  
the ID of the method to wait for

getBrokerName()
---------------

Gets the name of the parent broker.

### Returns

The name of the parent broker.

getUsage(name)
--------------

Gets the method usage string. This summarises how to use the method.

### Parameters

name  
The name of the method.

### Returns

A string that summarises the usage of the method.

getStiffnesses(names)
---------------------

Gets stiffness of a joint or group of joints.

### Parameters

names  
Name of a chain, ‘Body’, ‘BodyJoints’ or ‘BodyActuators’

### Returns

One or more stiffnesses. 1.0 indicates maximum stiffness. 0.0 indicated minimum stiffness

setStiffnesses(names, stiffnesses)
----------------------------------

Sets the stiffness of one or more joints. This is a non-blocking call.

### Parameters

names  
Name of a chain, ‘Body’, ‘BodyJoints’ or ‘BodyActuators’

stiffnesses  
One or more stiffnesses between zero and one.

stiffnessInterpolation(names, stiffnesses, timeLists)
-----------------------------------------------------

Interpolates one or multiple joints to a targeted stiffness or along timed trajectories of stiffness. This is a blocking call.

### Parameters

names  
Name or names of
