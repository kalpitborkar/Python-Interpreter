# Byterun
A compact Python Interpreter written in Python.

# About the project
## What is Byterun?
  - Byterun is a compact Python interpreter - a software that emulates a physical computer.
  - Byterun is a Python interpreter written in Python.
  - The Python interpreter is a virtual machine, in particular a stack machine - it manipulates several stacks to perform its operations.

## The purpose of this project is to learn and practice concepts related to:
- Working and structure of Python interpreter (CPython)
- Stack machine
- Python OOP

## Byterun structure:
There are four kinds of objects in Byterun:
### 1. `VirtualMachine` class:
  - The `VirtualMachine` class manages the highest level structure.
  - Manages the call stack of frames and contains a mapping of instructions to operations.
  - `VirtualMachine` stores the call stack, the exception state, and return values while they're being passed between frames.
### 2. `Frame` class:
  - Every `Frame` instance has one code object.
  - Manages:
    - The local, global, and builtin namespaces.
    - A reference to the previous frame.
    - A data stack.
    - A block stack.
    - The last instruction executed.
### 3. `Function` class:
  - Creates a new frame in the interpreter everytime a function is called.
  - Controls the creation of new `Frame` objects.
### 4. `Block` class:
  - A `Block` just wraps the three attributes of blocks - `type`, `handler` and `stack_height`
  - A `Block` is used for flow control, specifically exception handling and looping.
