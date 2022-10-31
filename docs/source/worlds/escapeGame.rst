.. _escapeGame.rst:

``escapeGame`` :bdg-primary:`medium`
####################################

..  admonition:: Description
    :class: tip

    This scenario is intended as a challenge once the US sensor is mastered. It
    requires a decent amount of code and a good strategy to escape from a big
    prison as the robot is initialy located at a random position and and headed
    in a random direction.

    It fosters problem and code decomposition.

..  admonition:: Source file

    https://github.com/informatiquecsud/21learning-components/blob/main/public/robotsim1/worlds/escapeGame.js

Specific query parameters
=========================

.. admonition:: Specific parameters

    - ``prisonWidth`` : Integer number indicating the width of the prison
    - ``prisonHeight`` : Integer number indicating the height of the prison
    - ``holeWidth`` : Integer number indicating the width of the hole
    

Small prison
============

The hole position is determined randomly.

..  pyrobotsim::
    :world: escapeGame
    :height: 700px
    :scrollx: -330
    :scrolly: -170
    :zoom: 3
    :hsplit: 500
    :vsplit: 1
    :extra_args: prisonWidth=600&prisonHeight=400&holeWidth=300

    from mbrobot import *

Large prison
============

..  pyrobotsim::
    :world: escapeGame
    :height: 700px
    :scrollx: -300
    :scrolly: -200
    :zoom: 0
    :hsplit: 500
    :vsplit: 1
    :extra_args: prisonWidth=1200&prisonHeight=800&holeWidth=300

    from mbrobot import *

