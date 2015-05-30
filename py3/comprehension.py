# There is not only list comprehension

li = [i for i in range(5)]

# set comprehension

se  = {i for i in range(10,0,-1)}

# dict comprehension

di = {i: i*i for i in range(10)}

def foo(n):
    return 'foo ' * n
# indeed, u can call a method
df = {i: foo(i) for i in range(10)}
