mmdevicetests
=============

A work in progress: tests for Micro-Manager device adapter modules

Goals
-----

In progress:

- Wrap the MMDevice interface so that device adapter binaries can be loaded and
  tested using Python code

Not started:

- Provide automated tests for basic functionality and consistency
  - E.g., do properties behave logically?
- Provide guided-tests for expected hardware behavior
  - E.g., does shutter open when commanded to open?

Non-goals
---------

- Providing a general purpose Python interface to device adapters (see pymmcore
  for that)
- Testing hardware performance or specs (the goal here is to test correctness of
  Micro-Manager device adapters, not the devices themselves)

Code of Conduct
---------------

This project is covered by the [Micro-Manager Code of Conduct](https://github.com/micro-manager/micro-manager/blob/master/CodeOfConduct.md).

License
-------

BSD-3 (see `LICENSE.txt`), which is the same license under which MMDevice (the
Micro-Manager device interface library) is released. Other parts of
Micro-Manager are under different licenses.
