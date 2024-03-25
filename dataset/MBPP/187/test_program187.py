from program187 import driver
def test0():
  assert driver("AGGTAB", "GXTXAYB", 6, 7, 4) == "PASSED"

def test1():
  assert driver("ABCDGH", "AEDFHR", 6, 6, 3) == "PASSED"

def test2():
  assert driver("AXYT", "AYZX", 4, 4, 2) == "PASSED"

