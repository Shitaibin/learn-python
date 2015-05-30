seq = ['1', '2', '3']
sep = '+'
s1 = sep.join(seq)
print(s1)

dirs = '', 'usr', 'bin'
s2 = '/'.join(dirs)
print(s2)

print('C:' + '\\'.join(dirs))
