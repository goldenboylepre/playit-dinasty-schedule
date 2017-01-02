# playit-dinasty-schedule
Documentation
=============

This repository contains a package for the automatic generating schedule
for the Play.it Dinasty keeper league.

The Play.it Dinasty is a keeper league originated in the early 
2000s thanks to the passionate NBA fans who have been discussing
USA sports at http://forum.playitusa.com/.

Therefore, this package (or parts of it)  can be used by other
leagues too, providing that they adapt the code to their configuration 
of teams and league.
.

Author
======

Vincenzo Francioso (goldenboylepre@gmail.com)


Disclaimer
==========

Warning!

This package works on Linux, but it has not been thoroughly tested!

Moreover, errors and exceptions are barely handled!

Therefore, please, use with care!


Dependencies
============

- Python 2.6+: http://www.python.org/

Examples
========

To generate a schedule with each team 
playing four games(2 away, 2 home) against every other team in the same conference 
and 
playing two games(1 away, 1 home) against every other team in the other conference

    python dinasty.py --schedule
