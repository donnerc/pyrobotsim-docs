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

..  code-block:: python

    from ast import *

    class _FindDefs(NodeVisitor):
        def __init__(self):
            self.defs={}

        def visit_FunctionDef(self,node):
            #print("Found def!",type(node.name))
            self.generic_visit(node)
            self.defs[node.name]=node.name

        def get_defs(self):
            return self.defs


    ### Code to translate simple python code to be async. n.b. right now only sleep calls and imports are async in practice
    # all calls to local functions are async as otherwise you can't run sleep in them
    class _MakeAsyncCalls(NodeTransformer):
        def __init__(self,call_table):
            self.call_table=call_table
            self.in_main=False

        def visit_AsyncFunctionDef(self,node):
            # ignore anything that is already async except for the main
            if node.name=='__async_main':
                self.in_main=True
                self.generic_visit(node)
                self.in_main=False
            return node

        def visit_ImportFrom(self,node):
            if not self.in_main:
                return node
            elements=[]
            elements.append(Tuple([Constant(node.module),Constant(None)],ctx=Load()))
            # first call async code to import it into pyodide, then call the original import statement to make it be available here
            newNode=[Expr(value=Await(Call(Name('aimport',ctx=Load()),args=[List(elements,ctx=Load())],keywords=[]))),node]
            return newNode

        def visit_Import(self,node):
            if not self.in_main:
                return node
            elements=[]
            for c in node.names:
                thisElement=Tuple([Constant(c.name),Constant(c.asname)],ctx=Load())
                elements.append(thisElement)
            # first call async code to import it into pyodide, then call the original import statement to make it be available here
            newNode=[Expr(value=Await(Call(Name('aimport',ctx=Load()),args=[List(elements,ctx=Load())],keywords=[]))),node]
            return newNode

        def visit_FunctionDef(self,node):
            #print("Found functiondef")
            self.generic_visit(node) # make sure any calls are turned into awaits where relevant
            return AsyncFunctionDef(name=node.name,args=node.args,body=node.body,decorator_list=node.decorator_list,returns=node.returns)

        def _parse_call(self,name):
            allNames=name.split(".")
            retVal=Name(id=allNames[0],ctx=Load())
            allNames=allNames[1:]
            #print(dump(retVal))
            while len(allNames)>0:
                retVal=Attribute(value=retVal,attr=allNames[0],ctx=Load())
                allNames=allNames[1:]
            #print(dump(retVal))
            return retVal


        def visit_Call(self, node):
            target=node.func
            make_await=False
            nameParts=[]
            while type(target)==Attribute:
                nameParts=[target.attr]+nameParts
                target=target.value
            if type(target)==Name:
                nameParts=[target.id]+nameParts
            target_id=".".join(nameParts)
            simple_name=nameParts[-1]
            if target_id in self.call_table:
                make_await=True
            elif simple_name in self.call_table:
                make_await=True
            if make_await:
                nameNodes=self._parse_call(self.call_table[target_id])
                #print("make await",target_id,node.args,node.keywords)
                newNode=Await(Call(nameNodes,args=node.args,keywords=node.keywords))
                return newNode
            else:
                # external library call, ignore
                return Call(node.func,node.args,node.keywords)


    class _LineOffsetter(NodeTransformer):
        def __init__(self,offset):
            self.offset=offset

        def visit(self, node):
            if hasattr(node,"lineno"):
                node.lineno+=self.offset
            if hasattr(node,"endlineno"):
                node.end_lineno+=self.offset
            self.generic_visit(node)
            return node


    # todo make this for multiple code modules (and maybe to guess class types from the code..)
    def __asyncify_sleep_delay(code_str,compile_mode='exec'):
        code_imports = "import asyncio\n"

        asleep_def = "async def __async_main():\n"

        extraLines=len(asleep_def.split("\n"))-1


        code_lines = []

        for line in code_str.splitlines():
            if 'import' in line.split('#')[0]:
                code_imports += line + '\n'
            else:
                code_lines += ["    "+line]

        all_code = code_imports
        all_code += asleep_def
        all_code += '\n'.join(code_lines)
        all_code += '\n'

        #all_code+="_loop.set_task_to_run_until_done(__async_main())\n"
        all_code+="asyncio.run(__async_main())\n"

        # print(all_code)

        oldTree=parse(all_code, mode='exec')

        defs=_FindDefs()
        defs.visit(oldTree)
        allDefs=defs.get_defs()
        # override sleep with asleep
        allDefs["sleep"]="asyncio.sleep"
        allDefs["delay"]="delay"
        allDefs["time.sleep"]="asyncio.sleep"
        newTree=fix_missing_locations(_MakeAsyncCalls(allDefs).visit(oldTree))
        newTree=_LineOffsetter(-extraLines).visit(newTree)

        with open('tree.dump', 'w') as f:
            f.write(dump(newTree))

        return newTree

        #return compile(newTree,filename="your_code.py",mode=compile_mode)

    def __strip_async_main(new_ast):
        code = unparse(new_ast)
        lines = code.splitlines()
        final_lines = []

        in_async_main = False

        for line in lines:
            #print("currentline", line)
            if not in_async_main:
                if line.startswith('async def __async_main()'):
                    in_async_main = True
                elif line.startswith('asyncio.run(__async_main())'):
                    continue
                else:
                    final_lines.append(line)
            elif in_async_main:
                if line.startswith('    '):
                    final_lines.append(line[4:])
                elif line == '':
                    final_lines.append(line)
                else:
                    in_async_main = False

            #print('lines', final_lines)


        return '\n'.join(final_lines)



    result = __asyncify_sleep_delay(code_to_compile,compile_mode='exec')
    __strip_async_main(result)


Further ressources
==================

- The papyros project uses service workers to handle the async calls. This could
  be a better alternative to the currently hacky way of implementing
  ``delay(ms)`` : https://github.com/dodona-edu/papyros

- SyncMessage used to implement ``time.sleep`` and reading input from the stdin
  : https://github.com/alexmojaki/sync-message