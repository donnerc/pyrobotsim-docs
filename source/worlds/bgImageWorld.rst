.. _emptyWorld.rst:

``bgImageWorld`` :bdg-secondary:`generic`
#########################################

This world is designed as a blank world without any obstacle but one background
image. This is usefull as a basis to create a virtual world in Python.

..  admonition:: Source file

    https://github.com/informatiquecsud/21learning-components/blob/main/public/robotsim1/worlds/bgImageWorld.js

Specific query parameters
=========================

This world provides the following specific query parameters:

..  admonition:: URL query parameters

    The following URL query parameters allow to configure the ``bgImageWorld``
    virtual world:

    - ``bg`` : URL (relative to the ``bg`` directory or absolute (including
      remote)). Background images available in the package are to be found at
      https://github.com/informatiquecsud/21learning-components/tree/main/public/robotsim1/worlds/bg


Demo
====

..  pyrobotsim::
    :world: bgImageWorld
    :height: 700px
    :hsplit: 400
    :vsplit: 30
    :scrollx: -180
    :scrolly: -110
    :zoom: -1
    :extra_args: bg=trail.gif&bgScale=1.4

    from mbrobot import *

    rightArc(0.3)

Load an external image by URL
=============================

..
    ..  admonition:: Future work

        This feature is not implemented yet. 


It is also possible to load an image from an external location publicly
accessible over the Internet. This example below loads the tree from https://i0.wp.com/sketchbooknation.com/wp-content/uploads/2013/12/howtodrawatree.jpg

..  warning:: 

    The external image must not be protected by CORS headers.

..  pyrobotsim::
    :world: bgImageWorld
    :height: 700px
    :hsplit: 400
    :vsplit: 30
    :scrollx: -180
    :scrolly: -110
    :zoom: -1
    :extra_args: bg=https://i0.wp.com/sketchbooknation.com/wp-content/uploads/2013/12/howtodrawatree.jpg&bgScale=1.4

    from mbrobot import *


Creating a virtual world using Python
=====================================

The *de factor* way of creating new virtual worlds is by creating a Javascript
file in the ``/public/robotsim1/worlds`` directory. Nevertheless, it is also
possible to use Python to populate an existing virtual world with additional
obstacles, marks on the ground or detection zones.

The following example showcases some of the features accessible from Python
through the ``sim`` object defined in ``mbrobot.py`` and in ``robotsim.py``.

.. note:: 

    The ``robotsim`` is mostly a convenience module. All the functions are
    accessible through the global ``sim`` object.

..  pyrobotsim::
    :world: bgImageWorld
    :height: 700px
    :hsplit: 400
    :vsplit: 30
    :scrollx: -180
    :scrolly: -110
    :files: mbrobot.py,robotsim.py
    :zoom: -1
    :extra_args: bg=roundpath.gif&bgScale=1.4

    from mbrobot import *
    from robotsim import *
    from pyodide import create_proxy

    nb_checks = 0

    # proxies the Python function to be called as callback by JS code
    # when robot hits checkpoint
    @create_proxy
    def handle_checkpoint():
        global nb_checks
        nb_checks += 1
        print(f"Robot on checkpoint {nb_checks} during simulation periods")
        

    def initWorld():
        setLocation(x=106, y=-208, angle=-45)
        sim.wallCircle(-280, -34, 40)
        sim.wallRect(240, 205, 80, 30, 45)
        sim.zoneCircle(
            -100, 200, 50, 
            handle_checkpoint,
            0x00ff00, 0.5
        )
        
        

    initWorld()

    print(getLocation())


Background images included
==========================

.. note::

    The following backgrounds can be directly imported with the parameter ``bg=<image_name>``

..  grid:: 3
    :gutter: 3

    ..  grid-item-card:: ant_track.png

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/ant_track.png
            :align: center
            :width: 100%

    ..  grid-item-card:: bg-shape-1.png

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/bg-shape-1.png
            :align: center
            :width: 100%

    ..  grid-item-card:: bg.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/bg.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: bg2.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/bg2.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: bg3.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/bg3.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: blackarea.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/blackarea.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: blacktapes.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/blacktapes.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: border.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/border.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: bridge.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/bridge.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: channel.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/channel.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: 50cm.png

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/circle-50cm.png
            :align: center
            :width: 100%

    ..  grid-item-card:: circle.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/circle.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: colorparcours.png

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/colorparcours.png
            :align: center
            :width: 100%

    ..  grid-item-card:: field1.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/field1.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: field2.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/field2.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: learntrack1.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/learntrack1.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: learntrack2.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/learntrack2.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: learntrack3.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/learntrack3.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: learntrack4.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/learntrack4.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: mazegrid.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/mazegrid.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: oval.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/oval.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: road.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/road.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: roadtest.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/roadtest.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: roboroad.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/roboroad.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: roundpath.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/roundpath.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: track.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/track.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: track1.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/track1.gif
            :align: center
            :width: 100%

    ..  grid-item-card:: 01.png

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/trail-01.png
            :align: center
            :width: 100%

    ..  grid-item-card:: trail.gif

        ..  figure:: https://github.com/informatiquecsud/21learning-components/raw/main/public/robotsim1/worlds/bg/trail.gif
            :align: center
            :width: 100%

