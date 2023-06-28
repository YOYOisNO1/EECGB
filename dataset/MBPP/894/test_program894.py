from program894 import driver
def test0():
  assert driver("1.2, 1.3, 2.3, 2.4, 6.5", [1.2, 1.3, 2.3, 2.4, 6.5]) == "FAILED"

def test1():
  assert driver("2.3, 2.4, 5.6, 5.4, 8.9", [2.3, 2.4, 5.6, 5.4, 8.9]) == "FAILED"

def test2():
  assert driver("0.3, 0.5, 7.8, 9.4", [0.3, 0.5, 7.8, 9.4]) == "FAILED"

