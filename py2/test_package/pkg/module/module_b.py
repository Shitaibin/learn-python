from .module_a import function1


def function2():
    print "This is function2 from module_b.\nAnd I'am going to call",
    print "function1, which import from intra-packge module_a."
    function1("function2")
