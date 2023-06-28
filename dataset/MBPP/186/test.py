from program186 import driver
def test0():
  assert driver("The quick brown fox jumps over the lazy dog.", ["fox"], "Matched!") == "PASSED"

def test1():
  assert driver("The quick brown fox jumps over the lazy dog.", ["horse"], "Not Matched!") == "PASSED"

def test2():
  assert driver("The quick brown fox jumps over the lazy dog.", ["lazy"], "Matched!") == "PASSED"

