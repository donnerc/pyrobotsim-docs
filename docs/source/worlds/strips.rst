.. _strips.rst:

``strips`` :bdg-primary:`medium`
################################

..  admonition:: Description
    :class: tip

    This is a more advanced scenario where the robot must traverse the strips by
    counting them. This level is appropriate for teaching or testing programming the
    robot with state as the robot must count state transitions from "light" to
    "dark" color on the ground.

..  admonition:: Source file

    https://github.com/informatiquecsud/21learning-components/blob/main/public/robotsim1/worlds/strips.js

Specific query parameters
=========================

.. admonition:: Specific parameters

    - ``level`` : integer choice in ``[0, 1, 2, 3]``
    
    Level 3 allows to customize the strips with the following parameters

    - ``stripWidth`` : Array of the form ``[min, max]`` for random range
    - ``stripGap`` : Array of the form ``[min, max]`` for random range
    - ``nbStrips`` : Array of the form ``[min, max]`` for random range
    - ``stripHeight`` : Integer representing the height of the strip in pixels

    ..  admonition:: Example query parameters for custom level

        ..  code-block:: plain
    
            level=3&stripWidth=[20,20]&nbStrips=[5,10]&stripGap=[50,50]&stripHeight=800
   



Demo level 0
============

..  pyrobotsim::
    :world: strips
    :height: 500px
    :scrollx: 300
    :scrolly: 0
    :zoom: -1
    :hsplit: 300
    :extra_args: level=0

    from mbrobot import *

Demo level 1
============

..  pyrobotsim::
    :world: strips
    :height: 500px
    :scrollx: 300
    :scrolly: 0
    :zoom: -1
    :hsplit: 300
    :extra_args: level=1

    from mbrobot import *

Demo level 2
============

..  pyrobotsim::
    :world: strips
    :height: 500px
    :scrollx: 300
    :scrolly: 0
    :zoom: -1
    :hsplit: 300
    :extra_args: level=2

    from mbrobot import *

Demo level 3 (Custom level)
===========================

Parameters used : ``level=3&stripWidth=[3,12]&nbStrips=[20,30]&stripGap=[5,10]&stripHeight=400``

..  pyrobotsim::
    :world: strips
    :height: 500px
    :scrollx: 300
    :scrolly: 0
    :zoom: -1
    :hsplit: 300
    :extra_args: level=3&stripWidth=[3,12]&nbStrips=[20,30]&stripGap=[5,10]&stripHeight=400

    from mbrobot import *
