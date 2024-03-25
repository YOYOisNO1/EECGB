from program257 import driver
def test0():
  assert driver(10, 20, [20, 10]) == "FAILED"

def test1():
  assert driver(15, 17, [17, 15]) == "FAILED"

def test2():
  assert driver(100, 200, [200, 100]) == "FAILED"

