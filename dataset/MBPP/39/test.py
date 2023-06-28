from program39 import driver
def test0():
  assert driver("aab", "aba") == "PASSED"

def test1():
  assert driver("aabb", "abab") == "PASSED"

def test2():
  assert driver("abccdd", "cdabcd") == "PASSED"

