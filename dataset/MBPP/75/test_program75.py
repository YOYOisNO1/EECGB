from program75 import driver
def test0():
  assert driver([[6, 24, 12], [7, 9, 6], [12, 18, 21]], 6, "[(6, 24, 12)]") == "FAILED"

def test1():
  assert driver([[5, 25, 30], [4, 2, 3], [7, 8, 9]], 5, "[(5, 25, 30)]") == "FAILED"

def test2():
  assert driver([[7, 9, 16], [8, 16, 4], [19, 17, 18]], 4, "[(8, 16, 4)]") == "FAILED"

