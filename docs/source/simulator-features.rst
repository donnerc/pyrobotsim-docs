.. _simulator-features.rst:

Simulator features
##################

..  warning::

    The PyRobotSim simulator is based on the maturity work of Noé Schaller at
    Collège du Sud (Swiss High School) [#maturitywork]_. It is therefore not a professional
    product and is not production ready in the software engineering sense.

    It is nevertheless far better, usable, flexible and realistic than the
    corresponding simulation environment currenty available in the TigerJython
    IDE [#tigerjythonide]_.

    The coding envionment embedding the robotsim Simulator is also an actively
    developped prototype far from beeing production ready. For now, its purpose
    is to test different scenarios and test the boundaries of what is doable
    with Pyodide.

Introduction
============

The robotsim robot simulator is a Javascript PhaserJS based project embedded in
PyRobotSim. PhaserJS is a popular Javascript game framework used to develop
browser based 2D games. It integrates the MatterJS physics engine [#matters]_ to handle
collision, forces and so on.

Moving the robot by mouse drag
==============================

The robot can be moved by mouse drag. The movement is not super intuitive
because the MatterJS simulated a physical spring attached to the robot at the
location of the click. Therefore, the mouse has to be seen as a means to apply a
physical force to the robot at the location where the mouse first clicked before
the drag and proportional to the distance between the cursor while dragging and
the application point of the force.

This is not ideal but reflects the way the underlying robotsim simulator
currently works.

..  tip::

    You can move the robot with the mouse while moving. From the robot
    perspective, the mouse is just another force applied to it with an invisible
    spring.

    Experiment with moving the robot by running the following example.

..  attention::

    Don't apply too much force on the robot. You could literally break it
    (virtually !!!)

..  pyrobotsim::
    :world: circle50cm
    :height: 400px
    :scrollx: -58
    :scrolly: -22
    :zoom: -3

    from mbrobot import *

    forward()


Camera control
==============

UI camera controls
------------------

The overlay scene of the robotsim simulation provide controls to alowing the
user to control the camera by hand.

..  margin::

    ..  figure:: figures/camera-controls.png
        :width: 100%
        :align: center

        Camera controls of the overlay scene



- Zoom (+/-)
- Camera scroll
- Camera mode : ``free`` of ``following`` the robot


Programmatic control
--------------------

The camera can be controlled programmatically as well with the ``camera`` object
defined in the ``mbrobot`` module.

..  warning::

    The camera control is obiously only available in the simulated environment
    and makes no sense on the physical robot. You can therefore run this code
    exlusively in simulated mode by checking the ``mode`` variable that is
    automatically set to the ``SIM`` constant in simulation mode and to ``REAL``
    on the physical robot.

..  pyrobotsim::
    :world: simpleTrail
    :height: 800px
    :vsplit: 40
    :hsplit: 300
    :zoom: -3
    :scrolly: -120
    :scrollx: 200

    from mbrobot import *

    def demo_zoom():
        if mode == SIM:
            for _ in range(4):
                delay(1000)
                print("Zooming out ...")
                overlayScene.zoomOut()

            for _ in range(3):
                delay(1000)
                print("Zooming in ...")
                overlayScene.zoomIn()
    

    def demo_camera_mode():
        if mode == SIM:
            print("Switch to free mode ...")
            overlayScene.freeMode()
            delay(3000)
            
            print("Switch to follow mode (following robot with index 0) ...")
            camera.x = robot.body.x
            camera.y = robot.body.y

            overlayScene.followMode(0)
            delay(3000)

    def demo_camera_scroll():
        # Control the camera directly
        for _ in range(3):
            print("Scrolling the camera allong the x axis ...")
            camera.scrollX += 200
            delay(1000)

            
        # Control the camera directly
        for _ in range(3):
            print("Scrolling the camera allong the y axis ...")
            camera.scrollY += 200
            delay(1000)


    demo_zoom()
    rightArc(0.2)
    demo_camera_mode()
    overlayScene.freeMode()
    demo_camera_scroll()
    camera.rotateTo(45)





Collision detection
===================

The objects of type ``Wall`` act as real walls. When the robot collides with a
wall, the effect on the robot is very similar to what happens in reality.

The following example demonstrates how the robot behaves when running into a
wall.

..  warning::

    In the ``slalom`` world used in the example, the camera is rotated 90°.
    Therefore, the :math:`x`-axis is vertical and the :math:`y`-axis is
    horizonzal. This explains why the ``robot.setPosition(10, 0)`` shifts the
    robot upwards.

..  tip:: 

    Run the program of the example to see how the obstacles (called "Walls" in
    robotsim) make the robot collide realistically.

..  pyrobotsim::
    :world: slalom
    :height: 400px
    :scrollx: 50

    from mbrobot import *

    if mode == SIM:
        robot.setPosition(50, 0)
        robot.setAngle(0)

    forward()

Front LEDs
==========

The maqueen:LITE robot is has front red LEDs which are simulated in robotsim.
They are controlled by writing a ``0`` (=OFF) or a ``1`` (=ON) on ``pin8``
(left) or ``pin12`` (right):

..  tip::

    For demonstration purpose, the following code uses the simulated microbit
    API directly to make the LEDs blink. The ``mbrobot`` module provides a
    convience function ``setLED`` to make that happen without bothering with the
    hardware pins.

..  pyrobotsim::
    :zoom: 5
    :scrollx: -280
    :scrolly: -230

    from microbit import pin8, pin12
    from delay import delay

    OFF, ON = 0, 1
    LEFT = pin8
    RIGHT = pin12

    def blink(led, n, duration=1000):
        for _ in range(n):
            led.write_digital(ON)
            delay(duration // n // 2)
            led.write_digital(OFF)
            delay(duration // n // 2)

    blink(LEFT, 4, 3000)
    blink(RIGHT, 4, 3000)


Ultrasonic sensor
=================

The maqueen:LITE robot is equiped with a virtual ultrasonic sensor at the front
capable of measuring ranges from 5 to roughly 400 cm. Nevertheless, the way the
``getDistance()`` function is currently beeing implemented only allows to detect
objects up to 255 cm. If no object is detected, the ``getDistance()`` function
returns the ``int`` value 255.

..  tip::

    Try to move the robot around with the mouse to see how the distance measured
    to objects in front of the robot varies.


..  pyrobotsim::
    :world: slalom
    :height: 600px
    :scrollx: 50
    :hsplit: 250

    from mbrobot import *

    while True:
        d = getDistance()
        print(f"Distance: {d}")
        delay(100)

Infrared sensors
================

The maqueen:LITE robot is equiped with two infrared sensors under the chassis.
Those two sensors are also simulated. They return either 0 or 1, 0 meaning
"dark" and 1 meaning "light". The sensor measure the quantity of reflected IR
light from the ground. In the virtual world, this is determined based on the
color of the pixels directly under the virtual sensors (with same coordinates).

..  tip:: 

    Run the code in the example and try to move the robot around. You can
    observe that the two indicator LEDs (in blue on the physical robot) are also
    simulated.

    To make the robot follow the line, add the following code after line 8:

    ::

        if vL == 0 and vR == 0:
            forward()
        elif vL == 1 and vR == 0:
            rightArc(0.1)
        elif vL == 0 and vR == 1:
            leftArc(0.1)
        else:
            backward()

..  pyrobotsim::
    :world: bgImageWorld
    :height: 700px
    :hsplit: 400
    :scrollx: -180
    :scrolly: -110
    :zoom: -1
    :extra_args: bg=trail.gif&bgScale=1.4

    from mbrobot import *

    setSpeed(45)
    while True:
        vL = irLeft.read_digital()
        vR = irRight.read_digital()

        print(f"Left sensor: {vL}\tRight sensor: {vR}")

        delay(100)
        
Footnotes
=========

..  [#maturitywork] GitHub repo of the maturity work :
    https://github.com/NoeSchaller/TM_Noe/blob/main/TM_code/V1-1/MaqueenSimulationV1-1.js


..  [#tigerjythonide] The home page of the TigerJython IDE is 
    https://tigerjython.ch/en and the IDE can be downloaded from https://tigerjython.ch/en/products/download

..  [#matters] The website of MatterJS can be found at https://brm.io/matter-js/ and many examples
    of integration in PhaserJS can be found at https://phaser.io/examples/v3/category/physics/matterjs.

