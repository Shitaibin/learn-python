# Put unittest files and orther files in different directorys.
# How to make it work.

# 1. make lib directory to be a package by using __init.py
# 2. append search directory to sys.path(BUT THIS MAY BE NOT A GOOD WAY)

import sys
sys.path.append("..")

import unittest

import lib.lib_file1 as lf

class LibFile1TestCase(unittest.TestCase):
    """
    """
    def test_function1(self):
        """
        """
        lf.function1()


if __name__ == '__main__':
    unittest.main()