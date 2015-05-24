class Person:
    name = 'unknown'
    
    def getName(self):
        return self.name

p1 = Person     #p1 just a another name of Person
print(p1.name)
#p1.getName()
print("type(p1): ", type(p1))

p2 = Person()
p2.name
print(p2.getName())
print("type(p2): ", type(p2))

p3 = p1()
p3.name
print(p3.getName())
print("type(p3): ", type(p3))
