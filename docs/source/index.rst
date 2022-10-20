..  PyRobotSim documentation
    sphinx-quickstart on Fri Nov 19 16:13:20 2021.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.
    

PyRobotSim docs
###############

..  dropdown:: See quick demo

    ..  tip::

        Before reading the documentation don't hesitate to take a look at this
        little demo showing the use of the simulated ultrasonic sensor. The
        program keeps the robot at good distance from the moving wall.

        To start de demo, click the RUN button to run the Python program on the
        virtual Maqueen:LITE robot.

        You can also take a look at the ``mbrobot.py`` file. This exact Pythom
        module runs on the virtual robot as well as on the physical robot
        without modification. Nevertheless, note that in order to run it on the
        physical robot, you need to minify (https://python-minifier.com/) it
        first to let it fit into micro:bit's tiny RAM. 

    ..  pyrobotsim::
        :world: experimentDistance
        :zoom: -4
        :width: 100%
        :scrollx: 330
        :vsplit: 45
        :hsplit: 400
        :height: 600px
        :files: mbrobot.py

        from mbrobot import *

        setSpeed(40)

        while True:
            # reading the US sensor and printing
            # the distance to the serial line
            d = getDistance()
            print(d)

            # keep good distance
            if d < 20:
                backward()
            else:
                forward()

            # wait 100 ms until next sensor read
            delay(100)

    

..
    ..  figure:: figures/demo-us-sensor.gif

..  toctree::
    :maxdepth: 2
    :caption: Simulation environment

    introduction.rst
    basic-features.rst
    simulator-features.rst
    how-it-works.rst
    share-and-configure.rst
    mbrobot-module.rst
    creating-virtual-world.rst

..  toctree::
    :maxdepth: 2
    :caption: Virtual worlds
    :glob:

    worlds/*
    



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
