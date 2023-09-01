#!/usr/bin/env python
"""
Sample script that uses the ConnectPython module created using
MATLAB Compiler SDK.

Refer to the MATLAB Compiler SDK documentation for more information.
"""

from __future__ import print_function
import ConnectPython
import matlab

my_ConnectPython = ConnectPython.initialize()

aIn = matlab.double([2.0], size=(1, 1))
bIn = matlab.double([3.0], size=(1, 1))
cOut = my_ConnectPython.ConnectPython(aIn, bIn)
print(cOut, sep='\n')

my_ConnectPython.terminate()