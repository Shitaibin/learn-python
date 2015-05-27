
def listfeature(module):
    return [n for n in dir(module) if not n.startswith('_')]


def listall(module):
    try:
        return module.__all__
    except:
        return None
    finally:
        return ['No __all__']

import copy     # for make example
# use help
help(copy)
help(copy.copy)

# print __doc__
print(copy.__doc__)
print(copy.copy.__doc__)
