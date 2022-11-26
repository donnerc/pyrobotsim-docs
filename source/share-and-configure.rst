.. _share-and-configure.rst:

Sharing, embedding and configuring
##################################

.. note::

    The aim of the PyRobotSim environment is to be easily embeddable in other Web
    documents, especially for writing robotics tutorials. Therefore, every aspect of
    the environment is configurable and shareable through the URL query parameters,
    including the contents of the ``main.py`` file.

    This allows super easy stateless solution sharing between teachers and
    students without any complicated server side stateful technology, and hence
    requiring no user authentication. 

URL query parameters reference
==============================

The following example demonstrates every aspect of the environment that is
configurable through the URL query parameters.

..  tip::

    Click the "Open in separate window" link below to open the environment in a
    new window and access the URL query parameters. You will see that the URL
    is as follows 

    ::

        https://21learning-components.surge.sh/#/component/PyRobotSim?angle=45&camera=free&files=mbrobot.py,microbit.py,mbalarm.py,robotsim.py&x=30&y=100&width=110%&height=700px&zoom=-1&hsplit=400&world=bgImageWorld&vsplit=30&main=ZnJvbSBtYnJvYm90IGltcG9ydCAqCgpwcmludCgiY291YyIp&scrollX=-180&scrollY=-110&bg=trail.gif&bgScale=1.4

..  admonition:: URL query parameters

    The following URL query parameters allow to configure the different aspect
    of the simulation:

    - ``main`` : base64 encoding of the ``main.py`` file contents    
    - ``world`` : virtual world to load. Available virtual worlds can be found
      at
      https://github.com/informatiquecsud/21learning-components/tree/worlds/public/robotsim1/worlds
    - ``files`` : files to show in the editor, comma separated. Example : ``mbrobot.py,microbit.py``
    - ``vsplit`` : position [percentage] of the vertical splitter between the
      editor (left) and the simulation (right)
    - ``hsplit`` : position [pixels] of the horizontal splitter between the
      simulation (top) and the output panels (bottom)
    - ``zoom`` : zoom level (+/- integer). This corresponds to the amount of
      clicks on the zoom In (+) or Zoom out (-) control.
    - ``x`` : initial :math:`x`-coordinate of the robot
    - ``y`` : initial :math:`y`-coordinate of the robot
    - ``angle`` : initial angle of the robot
    - ``scrollX`` : initial :math:`x`-scroll of the camera
    - ``scrollY`` : initial :math:`y`-scroll of the camera
    - ``camera`` : camera mode (``free`` or ``follow``)
    - ``robotType`` : robot to use. Can be one of (``lite`` for Maqueen:LITE or
      ``plus1`` for Maqueen:PLUS V1)


..  pyrobotsim::
    :world: bgImageWorld
    :height: 700px
    :hsplit: 400
    :vsplit: 30
    :camera: free
    :scrollx: -180
    :scrolly: -110
    :x: 30
    :y: 100
    :angle: 45
    :files: mbrobot.py,microbit.py,mbalarm.py,robotsim.py
    :zoom: -1
    :robot_type: plus1 
    :extra_args: bg=trail.gif&bgScale=1.4

    from mbrobot import *

World specific query parameters
===============================

Each virtual world can be further configured by specific query parameters
documented separatly for each virtual world.


