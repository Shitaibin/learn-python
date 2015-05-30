a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

z = zip(a, b, c)
for i, j, k in z:
    print(i, j, k)

c.pop()
print("c is:", c)

# the size of sequence can different
z = zip(a, b, c)
for i, j, k in z:
    print(i, j, k)
