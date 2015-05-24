words = ['cat', 'window', 'abcdefgh']
print(words)

# modify the list when using for
for w in words[:]:
    #print(w, len(w))
    if len(w) > 6:
        words.insert(0, w)


print(words)
