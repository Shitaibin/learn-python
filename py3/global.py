def foo(x):
    return x        # x still global

def change(x):
    return x+1      # x auto becomes to local

x = 1
y = foo(x)
z = change(x)

print("x = %d, y = %d, z = %d" % (x, y, z))
print("y is x: ", y is x)
print("z is x: ", z is x)


def change_global():
    global x
    x = x + 1 

change_global()
print("x = %d" % (x))
