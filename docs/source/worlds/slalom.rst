.. _emptyWorld.rst:

``slalom`` :bdg-primary:`beginner`
##################################

This is a beginner world designed to learn basic robot control. The robot must
slalom around the circular walls.

..  admonition:: Source file

    https://github.com/informatiquecsud/21learning-components/blob/main/public/robotsim1/worlds/slalom.js

Specific query parameters
=========================

There is no specific parameter for this virtual world.

Demo
====

..  pyrobotsim::
    :world: slalom
    :height: 600px
    :scrollx: -175
    :scrolly: -1015
    :zoom: -2

    from mbrobot import *

    forward()
    delay(1000)

    left()
    delay(560)
    stop()

    rightArc(0.25)
    delay(3800)
    stop()

    leftArc(0.25)
    delay(4200)
    stop()

    rightArc(0.25)
    delay(4200)
    stop()