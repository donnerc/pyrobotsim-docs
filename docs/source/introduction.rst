.. _introduction.rst:

Introduction
############

**PyRobotSim** is a 2D Web simulation environment for teaching robotics based on
the PhaserJS game framework and the Pyodide Python interpreter. It has
originally been designed with the Maqueen:lite and Maqueen:Plus robotics
platforms in mind. It is based on the following other projects:

- Pyodide (https://pyodide.org/en/stable/)
- PhaserJS Maqueen Simulation
  (https://github.com/NoeSchaller/TM_Noe/blob/main/TM_code/V1-1/MaqueenSimulationV1-1.js).
  This is a maturity work (Maturitätsarbeit / Travail de maturité) at Collège.

Project goals
=============

The goals of the project are the following:

- Teaching robotics without the physical robot. This is especially usefull when
  teaching basic principles in full class. The simulation therefore aims at
  beeing as realistic as possible using the MaterJS Physics engine integrated in
  PhaserJS.

- Support making robotics video tutorials

- Support robotics exams without the hassle and unreliability of low cost
  education robots

- Support remote teaching of robotics

- Allow students to do homework and study for the exam without the physical
  robot.

- Allowing interactive code examples to be embedded in textual tutorials and
  websites (see examples in this Sphinx documentation)

Project status
==============

Currently the PyRobotSim is under active development and at a prototypal phase.
It is already actively been used at Collège du Sud for teaching introductory
robotics but the codebase is far from beeing production ready. For example, the
there is no automated test suite.