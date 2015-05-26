def flatten(nested):
    try:
        try: nested+''
        except TypeError: pass
        else: raise TypeError       #nested like a str
        for sublist in nested:
            for elem in flatten(sublist):
                yield elem
    except TypeError:
        yield nested

l1 = list(flatten([[[1],2],3,4,[5,[6,7]],8]))
l2 = list(flatten([['foo',['bar']], ['bar', ['foo', ['foo']]]]))
