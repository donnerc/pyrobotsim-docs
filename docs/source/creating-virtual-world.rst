.. _creating-virtual-world.rst:

Creating a new virtual world
############################

This section explains how to build your own virtual world / scenario. There are
several was of creating new virtual worlds. 

#.  The most powerful way of creating virtual worlds is to program them directly
    in JavaSript (ECMAScript) as the underlying simulation engine is written in
    ES6 using the PhaserJS game framework.

#.  Loading a base virtual world like ``emptyWorld`` or ``bgImageWorld`` and
    customizing it directly in Python.

Writing a new virtual world using JS
====================================

The built-in virtual worlds are written in ES6 and available at
https://github.com/informatiquecsud/21learning-components/tree/main/public/robotsim1/worlds.
Each world is a single JS file implementing several callbacks corresponding to
different initialization phases of the game simulation.

..  _creating-virtual-world-example-01-circle:

Example 1 : ``circle50cm.js``
-----------------------------

This first example aims at explaining how the virtual world ``circle50cm``
has been created.

..  code-block:: javascript

    function mapLoad(scene, params) {
      scene.load.image("circle", "worlds/bg/circle-50cm.png");
    }
    
    function mapCreate(scene, params) {
      new Picture(scene, "circle", 0, 0, 0, 1.1, 1.1);
    }
    
    function sceneCreated({ overlayScene, robots }, params) {
      // simulates a click on the "freeMode" button
      overlayScene.freeMode();
      // simulates a click on the "+" button
      overlayScene.zoomIn();
      // overlayScene.camera.scrollY -= 200;
      robots[0].setPosition(230, 0);
    }


Important callbacks to build a virtual world
============================================

The example :ref:`creating-virtual-world-example-01-circle` shows the three main
callbacks every virtual world should define. These functions get called
automatically by the robotsim simulateur at different steps of the Phaser
simulation initialization.

The virtual world has to define the following callback functions

* ``mapLoad(scene, params)``
* ``mapCreate(scene, params)``
* ``sceneCreated(scene, params)``

Callback reference
------------------

..  js:function:: mapLoad(scene, params)
 
    :param Phaser.Scene scene: The main Phaser scene (see https://photonstorm.github.io/phaser3-docs/Phaser.Scene.html)
    :param URLSearchParams params: See https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams
    :returns: No value returned.
 
    The ``mapLoad`` callback is called first. Its purpose is to preload all the
    assets needed for the virtual world. This is mots useful to preload background
    images with the ``async`` function ``scene.load.image``. 

..  js:function:: mapCreate(scene, params)
 
    :param Phaser.Scene scene: The main Phaser scene (see https://photonstorm.github.io/phaser3-docs/Phaser.Scene.html)
    :param URLSearchParams params: See https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams
    :returns: No value returned.
 
    The ``mapCreate`` callback is called once the images have been downloaded and
    once the scene has been setup. This is the place to populate the world with
    elements like pictures, walls, marks and detection zones.

    
..  js:function:: sceneCreated(scene, params)
 
    :param Phaser.Scene scene: The main Phaser scene (see https://photonstorm.github.io/phaser3-docs/Phaser.Scene.html)
    :param URLSearchParams params: See https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams
    :returns: No value returned.
 
    The ``sceneCreated`` callback is called once the scene has been created and the
    robot is positioned at the origin heading upwards. This is the right place to
    adjust details like the zoom factor or the camera scrolling to make the world
    fit into the screen.


The ``scene`` API
=================

All three callbacks receive a ``Simul`` instance that inherits from
``Phaser.Scene`` instance as first argument. 

..  admonition:: Source code

    See the ``Simul`` class definition :
    https://github.com/informatiquecsud/21learning-components/blob/main/public/robotsim1/MaqueenSimulationV1-1.js#L124

Essential ``Simul`` methods and attributes
------------------------------------------

..  js:function:: scene.load.image(key, url, [xhrSettings])
 
    :param string key: A string representing a unique identifier for the image once loaded.
    :param string url: A string representing the location where to get the image file from.
    :param 	Phaser.Types.Loader.XHRSettingsObject | false xhrSettings: Custom XHR parameters. See https://photonstorm.github.io/phaser3-docs/Phaser.Types.Loader.html#.XHRSettingsObject
    :returns: The ``Phaser.Loader.LoaderPlugin`` loader instance

    Adds the image specified by ``url`` to the load queue. See also
    https://photonstorm.github.io/phaser3-docs/Phaser.Loader.LoaderPlugin.html#image__anchor


Global ``simulation`` object
============================

There is a global ``sim`` instance of class ``simulation``
(https://github.com/informatiquecsud/21learning-components/blob/main/public/robotsim1/MaqueenSimulationV1-1.js#L1)
that is created before the callbacks are called. The global ``sim`` object is
therefore accessible from within the callbacks.

..  warning::

    As a class, the ``simulation`` should have been called ``Simulation``. Maybe
    this could change in a future version.

Walls
-----

..  js:function:: sim.wallCircle(x, y, r)

    Adds a new circular wall to the scene. A wall can be detected by the US to
    measure distances to the wall. Moreover, the robot cannot go through the
    wall that acts like a fixed unmovable physical obstacle.

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created game object.
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created game object. 
    :param Number r: Radius of the initial position for the created game object. 
    :returns: The created ``wallCircle`` instance

    
..  js:function:: sim.wallRect(x, y, width, height, angle=0)

    Adds a new rectangular wall to the scene. A wall can be detected by the US
    to measure distances to the wall. Moreover, the robot cannot go through the
    wall that acts like a fixed unmovable physical obstacle.

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created game object. 
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created game object. 
    :param Number width: Initial width of the created rectangle mark. 
    :param Number height: Initial height of the created rectangle mark. 
    :param Number angle: Initial angle of the created rectangle mark. 
    :returns: The created ``wallRect`` instance

..  js:function:: sim.wallPoly(x, y, points)

    Adds a new polygonal wall to the scene. A wall can be detected by the US to
    measure distances to the wall. Moreover, the robot cannot go through the
    wall that acts like a fixed unmovable physical obstacle.

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created polygon. 
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created polygon. 
    :param Phaser.Types.Math.Vector2Like points: Coordinates of the polygon
        vertices relative to the :math:`(x, y)` coordinates. See
        https://photonstorm.github.io/phaser3-docs/Phaser.Types.Math.html#.Vector2Like
        and https://photonstorm.github.io/phaser3-docs/Phaser.Geom.Polygon.html
    :returns: The created ``wallPoly`` instance

Marks
-----

..  js:function:: sim.markCircle(x, y, r)

    Adds a new circular mark to the scene. A mark is an object on the ground the
    robot can go through. The robot can use the infrared sensor to measure the
    darkness of the mark. A mark is either dark (0) or light (1).
    

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created game object.
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created game object. 
    :param Number r: Radius of the initial position for the created game object. 
    :returns: The created ``markCircle`` instance

    
..  js:function:: sim.markRect(x, y, width, height, angle=0)

    Adds a new rectangular mark to the scene. A mark is an object on the ground the
    robot can go through. The robot can use the infrared sensor to measure the
    darkness of the mark. A mark is either dark (0) or light (1).

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created game object. 
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created game object. 
    :param Number width: Initial width of the created rectangle mark. 
    :param Number height: Initial height of the created rectangle mark. 
    :param Number angle: Initial angle of the created rectangle mark. 
    :returns: The created ``markRect`` instance

..  js:function:: sim.markPoly(x, y, points)

    Adds a new polygonal mark to the scene.  A mark is an object on the ground
    the robot can go through. The robot can use the infrared sensor to measure
    the darkness of the mark. A mark is either dark (0) or light (1).
    

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created polygon. 
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created polygon. 
    :param Phaser.Types.Math.Vector2Like points: Coordinates of the polygon
        vertices relative to the :math:`(x, y)` coordinates. See
        https://photonstorm.github.io/phaser3-docs/Phaser.Types.Math.html#.Vector2Like
        and https://photonstorm.github.io/phaser3-docs/Phaser.Geom.Polygon.html
    :returns: The created ``markPoly`` instance

Detection zones that trigger a function on collision
----------------------------------------------------

..  js:function:: sim.zoneCircle(x, y, r, callback, color=0xff0000, alpha=0.3)

    Adds a new circular zone to the scene. A detection zone is a region of the
    virtual world the robot can go through. When the robot collides with the
    detection zone, the callback is fired.

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created game object.
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created game object. 
    :param Number r: Radius of the initial position for the created game object. 
    :returns: The created ``zoneCircle`` instance

    
..  js:function:: sim.zoneRect(x, y, width, height, angle, callback, color=0xff0000, alpha=0.3)

    Adds a new rectangular zone to the scene. A detection zone is a region of
    the virtual world the robot can go through. When the robot collides with the
    detection zone, the callback is fired.

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created game object. 
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created game object. 
    :param Number width: Initial width of the created rectangle mark. 
    :param Number height: Initial height of the created rectangle mark. 
    :param Number angle: Initial angle of the created rectangle mark. 
    :param callback callback: Function to call when the robot collides with the detection zone.
    :param int color: Hex number of the form ``0x------`` of the RGB code for
        the desired color. (Example: ``0xff00ff`` for magenta)
    :param Number alpha: Number between 0 and 1 to indicate the transparency
        (0=not transparent, 1=fully transparent)
    :returns: The created ``zoneRect`` instance

..  js:function:: sim.zonePoly(x, y, points, callback, color=0xff0000, alpha=0.3)

    Adds a new polygonal zone to the scene. A detection zone is a region of the
    virtual world the robot can go through. When the robot collides with the
    detection zone, the callback is fired.

    :param Number x: :math:`x`-coordinate of the initial position of the center of the created polygon. 
    :param Number y: :math:`y`-coordinate of the initial position of the center of the created polygon. 
    :param Phaser.Types.Math.Vector2Like points: Coordinates of the polygon
        vertices relative to the :math:`(x, y)` coordinates. See
        https://photonstorm.github.io/phaser3-docs/Phaser.Types.Math.html#.Vector2Like
        and https://photonstorm.github.io/phaser3-docs/Phaser.Geom.Polygon.html
    :param callback callback: Function to call when the robot collides with the detection zone.
    :param int color: Hex number of the form ``0x------`` of the RGB code for
        the desired color. (Example: ``0xff00ff`` for magenta)
    :param Number alpha: Number between 0 and 1 to indicate the transparency
        (0=not transparent, 1=fully transparent)
    :returns: The created ``zonePoly`` instance
