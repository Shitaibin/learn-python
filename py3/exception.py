# version 1
try:
    print('version 1')
    x = int(input('enter x: '))
    y = int(input('enter y: '))

    x / y
except (ZeroDivisionError, TypeError, NameError):
    print("your numbers were bogus...")

# version 2
try:
    print('version 2')
    x = int(input('enter x: '))
    y = int(input('enter y: '))

    x / y
except ZeroDivisionError:
    print("The second number can't be zero")
except TypeError:
    print("That wasn't a number, was it?")
except NameError:
    print("Here is a name error")

# version 3
try:
    print('version 3')
    x = int(input('enter x: '))
    y = int(input('enter y: '))

    x / y
except (ZeroDivisionError, TypeError, NameError) as e: # take an exception object e
    print("your numbers were bogus...")
    print("e: %s" % e)


#version 4
try:
    print('it will goes right')
except:
    print('sth wrong')
else:                               # add an else, it goes with no exception
    print('It went as planned. No exception')
finally:                            # add a finally, it goes with except,
    print('Cleaning up')            # it is used to closing file and socket
