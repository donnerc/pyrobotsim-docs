.. _basic-features.rst:

Basic usage
###########

..  admonition:: Simulation environment

    You can find a running version of PyRobotSim running at 
    
    ..  raw:: html

        <a target="_blank"
        href="https://21learning-components.surge.sh/#/component/PyRobotSim">https://21learning-components.surge.sh/#/component/PyRobotSim</a>

    ..  only:: latex

        https://21learning-components.surge.sh/#/component/PyRobotSim


Programming the virtual robot
=============================

The simulation environment reflects the way the Maqueen robot is programmed when
controlled by the micro:bit under the MicroPython firmware. On other words, the
program has to be written in the ``main.py`` file  which is automatically run
whenever the robot is switched on or reset.

Therefore, the code to program the virtual robot has to be written in the
``main.py`` file. Once the code is ready, click on the "RUN" button.

..  note:: 

    The Python interpreter used is pyodide. For now, the Python program is not
    run in a web worker. Therefore, once a pyodide program is started, there is
    no easy way to interrupt it or stop it. Nonetheless, robotics program are
    very often based on an infinite loop that polls the sensors:

    ..  code-block:: python

        from mbrobot import *

        while True:
            # Read value from the US sensor
            d = getDistance()

            # do something with the value

            # wait until next sensor read
            delay(100)

    Unless the code is run in a separate web worker (to be done in a future
    version), there is no other way of stopping a program than reloading the
    page. Use the "SHARE" button if you don't want to loose your changes to the
    ``main.py`` file (See :ref:`sec-share-main-py`).

.. _sec-share-main-py:

Sharing the ``main.py`` file
============================

You can easily share the contents of your ``main.py`` file with others by
clicking on the "SHARE" button. This encodes the contents of the ``main.py``
file as base64 and puts the corresponding string in the URL as ``main`` query
parameter.

..  admonition:: Exemple

    If the code in the ``main.py`` file is 

    ::

        from mbrobot import *

        forward()
        delay(1000)
        stop()

    clicking on the "SHARE" button will encode the file as 

    ::

        ZnJvbSBtYnJvYm90IGltcG9ydCAqCgpmb3J3YXJkKCkKZGVsYXkoMTAwMCkKc3RvcCgpCg==

    and put this string into the ``main`` query parameter in the URL. This means
    that the following link will bring directly to the code

    ..  admonition:: Link to the file

        ..  raw:: html
            
            <a target="_blank" href="https://21learning-components.surge.sh/#/component/PyRobotSim?main=ZnJvbSBtYnJvYm90IGltcG9ydCAqCgpmb3J3YXJkKCkKZGVsYXkoMTAwMCkKc3RvcCgpCg==">https://21learning-components.surge.sh/#/component/PyRobotSim?main=ZnJvbSBtYnJvYm90IGltcG9ydCAqCgpmb3J3YXJkKCkKZGVsYXkoMTAwMCkKc3RvcCgpCg==</a>


The module ``mbrobot.py``
=========================

In addition to the ``main.py`` file, the editor also shows the ``mbrobot.py``
Python module. This is the exact same file as the one available on the
micro:bit. There is also a file named ``microbit.py`` that simulates some
essential features of the micro:bit and necessary for the ``mbrobot.py`` module
to run correctly.

..  note::

    The ``microbit.py`` file is not shown by default in the editor but is
    nevertheless loaded to run the code. 

    In a future version, the will be query parameters to choose which files to
    open in the editor. At this stage, only the ``mbrobot.py`` file is shown in
    the editor.



Python modules
==============

All standard Python modules made available by default by the Pyodide interpreter
can be imported. Moreover, the files available at
https://github.com/informatiquecsud/21learning-components/tree/main/public/mbrobot
can also be imported.