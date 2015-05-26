
# construction method
class Bird:
    def __init__(self):
        self.var = 42
        print('Bird')

print("a new bird")
bird = Bird()

class BlackBird(Bird):
    def __init__(self):
        print('BlackBird')

print("\na new blackbird")
bbird = BlackBird()

class WhiteBird(Bird):
    def __init__(self):
        super(WhiteBird, self).__init__()     # call the construction method of his parent class, or it will 
        print('WhiteBird')

print("\na new whitebird")
wbird = WhiteBird()


# inherit
class CounterList(list):
    def __init__(self, *args):              # care of the parameters 
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)  # super other methods

counter = CounterList(range(10))
print(counter)
counter.reverse()
del counter[1:2]
print(counter)
print(counter.counter)
print(counter[1] + counter[4])
print(counter.counter)

