from program874 import driver
def test0():
  assert driver("abcabcabc", "abc", True) == "PASSED"

def test1():
  assert driver("abcab", "abc", False) == "PASSED"

def test2():
  assert driver("aba", "ab", False) == "PASSED"

