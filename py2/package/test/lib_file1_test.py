# Put unittest files and orther files in different directorys.
# How to make it work.

# 1. make lib directory to be a package by using __init__.py
# 2. append search directory to sys.path(BUT THIS MAY BE NOT A GOOD WAY)

########################################
# See pep328, pep338, pep366
########################################

# import sys
# sys.path.append("..")


# way 1: import module
from ..lib import lib_file1 as lf
lf.function1()

# way 2: from module import function
from ..lib.lib_file1 import function1

# way 3: from package import function
# see ../lib/__init__.py, I set all,
# so I can using function1 without explict
# import lib_file1
from ..lib import function1
function1()