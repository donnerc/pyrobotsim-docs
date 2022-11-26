.. _how-it-works.rst:

How it works
############

This section explains how the Python code of the ``main.py`` file is executed
with pyodide, in particular how the ``delay(ms)`` function is implemented in
order to overcome the limitation that Pyodide does not support the
``time.sleep(s)`` function of the standard Python ``time`` module.

Running async code
==================

The Pyodide interpreter, due to the execution model of the Browser, cannot
support the ``time.sleep(s)`` function. In order to pause the program, we
therefore "asyncify" the Python code to use the ``sleep(s)`` function of the
Python ``asyncio`` module.

..  tip::

    To see the "asyncified" code, run the code and activate the "ASYNC" tab of
    the right panel.

..  pyrobotsim::
    :files: mbrobot.py,delay.py
    :height: 300px
    :hsplit: 10
    :vsplit: 50

    from delay import delay

    def greet(name):
        print("Hello ")
        delay(1000)
        print(name)    

    greet("Dennis")

Code asyncification
===================

Before running the code, the code is beeing transformed according to following
rules:

- All functions are defined with the ``async`` keyword
- All function calls are preceded by the ``await`` keyword

..  grid:: 2
    :gutter: 1

    ..  grid-item-card:: Synchronous Python code

        ::

            from delay import delay

            def greet(name):
                print("Hello ")
                delay(1000)
                print(name)    

            greet("Dennis")

    ..  grid-item-card:: Asynchronous Python code

        ::

            import asyncio
            from delay import delay


            async def greet(name):
                print('Hello ')
                await delay(1000)
                print(name)
            await greet('Dennis')

Drawbacks
---------

This approach has several drawbacks:

- The runtime errors (Exceptions) are reported according the actual asyncified
  version and not the original version. The line numbers therefore currently
  often do not match correctly the original code.

  ..  admonition:: Planned workaround

      A simple work around could be to auto-format the code on the right the
      same as the async code is beeing formatted after the AST transformations.

      Another approach could be to build a "source map" to map line numbers of
      the async code to line numbers of the original code.

- It is not possible to define new classes, because the ``__init__``
  "constructor" will also be made async, which is actually not allowed in
  Python.

  ..  admonition:: Planned workaround

      The transformation could be a little less "greedy" and only transform
      functions containing calls to an other async functions. Nevertheless, this
      is easier said than done.

AST Transformation
==================

This section explains how exactly the code is transformed. It basically uses the
following Python code running in the Pyodide environment 

.. literalinclude:: scripts/asyncify.py
   :language: python



Further ressources
==================

- The trick currently is based on the ideas presented on
  https://joemarshall.github.io/pyodide-async/

- The papyros project uses service workers to handle the async calls. This could
  be a better alternative to the currently hacky way of implementing
  ``delay(ms)`` : https://github.com/dodona-edu/papyros

- SyncMessage used to implement ``time.sleep`` and reading input from the stdin
  : https://github.com/alexmojaki/sync-message

- Helper for running pyodide in a web worker and interrupting code :
  https://github.com/alexmojaki/pyodide-worker-runner. Uses ``sync-message``
  internally.

- https://blog.stackblitz.com/posts/cross-browser-with-coop-coep/ |
  https://github.com/WICG/credentiallessness