from program120 import driver
def test0():
  assert driver([[2, 7], [2, 6], [1, 8], [4, 9]], 36) == "PASSED"

def test1():
  assert driver([[10, 20], [15, 2], [5, 10]], 200) == "PASSED"

def test2():
  assert driver([[11, 44], [10, 15], [20, 5], [12, 9]], 484) == "PASSED"

