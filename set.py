s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)


s2 = {1,2,3,4,5,6}

s3 = set([1,2,3,4])


m = [ n for n in dir(set) if not n.startswith('_')]
print(m)


print('\n\nu can use this operators: &, |, -, ^')
