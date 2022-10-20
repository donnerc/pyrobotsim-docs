.. _emptyWorld.rst:

``between2walls``
#################

This is a beginner world designed to learn basic robot control and distance
measuring with the US sensor. The robot must go from one wall to the other
infinitely.

..  admonition:: Source file

    https://github.com/informatiquecsud/21learning-components/blob/main/public/robotsim1/worlds/between2walls.js

Specific query parameters
=========================

There is no specific parameter for this virtual world.

Demo
====

..  pyrobotsim::
    :world: between2walls
    :height: 600px
    :scrollx: -165
    :scrolly: 40
    :zoom: -1
    :hsplit: 300

    from mbrobot import *
    from mbalarm import *

    TIME_FOR_90_DEG = 550

    while True:
        forward()
        d = getDistance()
        
        print(d)
        
        if d < 10:
            stop()
            setAlarm(1)
            delay(1000)
            setAlarm(0)
            
            # rotation de 180°
            right()
            delay(2 * TIME_FOR_90_DEG)
            forward()
            
        delay(20)