# Put unittest files and orther files in different directorys.
# How to make it work.

# 1. make module directory to be a package by using __init__.py
# 2. append search directory to sys.path(BUT THIS MAY BE NOT A GOOD WAY)

########################################
# See pep328, pep338, pep366
########################################

# import sys
# sys.path.append("..")


# way 1: import module
# from ..module import module_a as ma
# ma.function1()

# way 2: from module import function
# from ..module.module_a import function1

# way 3: from pkg import function
# see ../module/__init__.py, I set all,
# so I can using function1 without explict
# import module_a
# from ..module import function1
# function1()

import unittest
import module
# from module import function1

# class ModuleATestCase(unittest):
#     def test_function1(self):
#         print "Call function1 of module_a from unittest"
#         module.function1("test_function1")
#
# if __name__ == "__main__":
#     unittest.m
# ain()