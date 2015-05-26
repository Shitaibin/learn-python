def foo():
    print("method has been called in test")

def test():
    foo()

# this is for test this python code, __name__ is '__main__' only when you run this code directly
if __name__ == '__main__':  
    test()
