# Write a Python program to find the location of Python module sources.

import os

print("location of python module and sources : ")
print(imp.find_module('os'))
print("location of the python module is  :")
print(imp.find_module('datetime'))
