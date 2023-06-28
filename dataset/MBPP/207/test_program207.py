from program207 import driver
def test0():
  assert driver("AABEBCDD", 3) == "PASSED"

def test1():
  assert driver("aabb", 2) == "PASSED"

def test2():
  assert driver("aab", 1) == "PASSED"

