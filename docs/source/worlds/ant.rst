.. _ant.rst:

``ant`` :bdg-primary:`advanced`
###############################

..  admonition:: Description
    :class: tip

    This is a rather advanced scenario, where a naive stateless approach does
    not work. The aim of the scenario is to program to robot to let it follow
    the "ant" track, that is a track formed by marks on the ground with space in
    between. The fact that the robot only "sees" a mark when the IR sensors pass
    over it avoids any kind of "planning". There for, the decisions and strategy
    cannot only depend on the values measured by the IR sensor but has to rely
    on another context related information, that is to say state.

    This world is a good opportunity to motivate state diagrams and to learn how
    to implement a a program where decisions also depend on the state of one or
    several variables.

..  admonition:: Source file

    https://github.com/informatiquecsud/21learning-components/blob/main/public/robotsim1/worlds/ant.js

Specific query parameters
=========================

.. admonition:: Specific parameters

    - ``level`` : integer choice in ``[0, 1, 2, 3]``
    

Demo level 0
============

The track is generated randomly each time. The track always turns to the right
only. The track pieces are have a decent width and length that don't vary too
much.

..  pyrobotsim::
    :world: ant
    :height: 700px
    :scrollx: 100
    :scrolly: 260
    :zoom: -1
    :hsplit: 500
    :vsplit: 1
    :extra_args: level=0

    from mbrobot import *

Demo level 1
============

The track is generated randomly each time. The track always turns to the left
only. The track pieces are slightly thinner and their length and spacing varies
a little more than level 0.


..  pyrobotsim::
    :world: ant
    :height: 700px
    :scrollx: -220
    :scrolly: -760
    :zoom: -2
    :hsplit: 500
    :vsplit: 1
    :extra_args: level=1

    from mbrobot import *

Demo level 2
============

The track is generated randomly each time. From this level on, the track may
turn left or right. The length and spacing between the pieces vary even more.

..  pyrobotsim::
    :world: ant
    :height: 700px
    :scrollx: 900
    :scrolly: -50
    :zoom: -4
    :hsplit: 500
    :vsplit: 1
    :extra_args: level=2

    from mbrobot import *

Demo level 3
============

The track is generated randomly each time. From this level on, the track may
turn left or right. The length and spacing between the pieces vary even more.
Some pieces are super thin.


..  pyrobotsim::
    :world: ant
    :height: 700px
    :scrollx: 900
    :scrolly: -50
    :zoom: -4
    :hsplit: 500
    :vsplit: 1
    :extra_args: level=3

    from mbrobot import *

..
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
        :vsplit: 1
        :extra_args: level=3&stripWidth=[3,12]&nbStrips=[20,30]&stripGap=[5,10]&stripHeight=400

        from mbrobot import *
