from program113 import driver
def test0():
    assert driver("python", False)

def test1():
    assert driver("1", True)

def test2():
    assert driver("12345", True)

