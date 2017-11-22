RobocupVision
#############

:version: 2.1.2

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

getDescription()
================
gets module description message


Returns
-------
description

getVisionResults(cameraId)
==========================
Returns the vision results for the given camera.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
vision result as list of integer list

getYUV422Image(cameraId)
========================
Returns an image in yuv422 format.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
image as byte array

getYUV422ImageWithTime(cameraId)
================================
Returns an image in yuv422 format with time.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
[[tv_sec, tv_usec], image as byte array]

getYUV422ImageWithTimeCameraMatrixAndBodyContour(cameraId)
==========================================================
Returns an image in yuv422 format with time, camera matrix and body contour.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
[[tv_sec, tv_usec], image as byte array, camera matrix, body contour]

getBGR24Image(cameraId)
=======================
Returns an image in bgr24 format.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
image as byte array

getBGR24ImageWithTime(cameraId)
===============================
Returns an image in bgr24 format with time.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
[[tv_sec, tv_usec], image as byte array]

getReducedYUV422Image(cameraId)
===============================
Returns an reduced image in yuv422 format.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
image as byte array

getReducedBGR24Image(cameraId)
==============================
Returns an reduced image in bgr24 format.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
image as byte array

getReducedBGR24ImageWithTime(cameraId)
======================================
Returns an reduced image in bgr24 format with time.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
[[tv_sec, tv_usec], image as byte array]

getAugmentedRealityMarkers(cameraId)
====================================
Returns ArUco augmented reality markers with time.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
[[tv_sec, tv_usec], markers]

setCameraConfiguration(cameraId, key, value)
============================================
Sets camera configuration.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:key: camera configuration key
:value: camera configuration value


getCameraConfiguration(cameraId, key)
=====================================
Gets camera configuration.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:key: camera configuration key

Returns
-------
camera configuration value

setVisionConfiguration(cameraId, key, value)
============================================
Sets vision configuration.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:key: vision configuration key
:value: vision configuration value


setConfig(list of key value pairs)
==================================
Sets configuration.

Parameters
----------
:list of key value pairs: [[key0, value0], [key1, value1], ...]


getVisionConfiguration(cameraId, key)
=====================================
Gets vision configuration.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:key: vision configuration key

Returns
-------
vision configuration value

getConfig(key)
==============
Gets configuration.

Parameters
----------
:key: camera_name.group.key_name

Returns
-------
configuration value

getAllConfig()
==============
Gets all vision configuration.


Returns
-------
configuration value

setCameraInfo(cameraId, key, value)
===================================
Sets camera info (intrinsic matrix and distortion coefficients).

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:key: configuration key
:value: configuration value


getCameraInfo(cameraId, key)
============================
Gets camera info (intrinsic matrix and distortion coefficients).

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:key: configuration key

Returns
-------
configuration value

setAugmentedRealityConfiguration(cameraId, key, value)
======================================================
Sets augmented reality configuration.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:key: augmented reality configuration key
:value: augmented reality configuration value


getAugmentedRealityConfiguration(cameraId, key)
===============================================
Gets augmented reality configuration.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:key: augmented reality configuration key

Returns
-------
augmented reality configuration value

enableVisionProcessing(cameraId, enable)
========================================
enable/disable vision processing.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:enable: enable


isVisionProcessingEnabled(cameraId)
===================================
Is vision processing enabled?

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera


enableCameraMatrixUsage(cameraId, enable)
=========================================
enable/disable the camera matrix usage in the vision processing.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:enable: enable


isCameraMatrixUsageEnabled(cameraId)
====================================
Is the camera is used in the vision processing??

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera


setVideoRecording(cameraId, enable)
===================================
enable/disable video recording.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera
:enable: enable


isVideoRecording(cameraId)
==========================
Is video recording enabled?

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera


writeCurrentConfigurationsIntoPrefFile()
========================================
Writes the current vision and camera settings into the preference file.



saveConfig()
============
Writes the current vision and camera settings into the preference file.



snapshot()
==========
snapshot one frame of image



getBodyContours(cameraId)
=========================
Returns the body contours.

Parameters
----------
:cameraId: 0 for top camera and 1 for bottom camera

Returns
-------
body contours as list of integer list
