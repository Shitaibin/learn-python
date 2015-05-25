class C:
    def __init__(self):
        self._x = None
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

c = C()
print(c.x)  # property,getter
c.x = 1     # setter
print(c.x)  # property,getter
del c.x     # deleter
#print(c.x)  # property,getter
