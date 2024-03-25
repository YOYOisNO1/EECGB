from program121 import driver
def test0():
    assert driver([2, 7, 4, 0, 9, 5, 1, 3], 8, 6, 0, True)

def test1():
    assert driver([1, 4, 5, 6, 7, 8, 5, 9], 8, 6, 0, False)

def test2():
    assert driver([10, 4, 2, 3, 5], 5, 15, 0, True)

