.. htmlwhat documentation master file, created by
   sphinx-quickstart on Sun Feb 11 13:32:50 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to htmlwhat's documentation!
====================================

This is the official documentation for htmlwhat. For an introductory setup, visit the `README <https://github.com/arlarse/htmlwhat>`_.

``htmlwhat`` is a Python library that is used to verify HTML code submissions. 
It's often used in educational platforms where students submit HTML code as part of their assignments or exercises.

The library provides a set of functions that can be used to write tests for HTML code. 
These tests can check for various things, such as whether the code contains tags, attributes, 
or text and provides meaningful feedback if the user submits incorrect code, 
helping them learn in the right direction.


.. toctree::
   :maxdepth: 2
   :caption: Quick Start

   articles/getting_start.rst

.. toctree::
   :maxdepth: 2
   :caption: Basic Articles

   articles/basics.rst
   articles/how_to_write_test.rst
   articles/electives.rst


.. toctree::
   :maxdepth: 2
   :caption: Acvanced Articles

   articles/check_multiple_tags.rst