class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 10:
        print(f)
        break

it = iter(Fibs())  #create a iterator from an iteratorable object
it.__next__()
print(it)
print(it.__next__())

