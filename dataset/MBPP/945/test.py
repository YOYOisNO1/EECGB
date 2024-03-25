from program945 import driver
def test0():
  assert driver(['x', 'y', 'z'], set(['y', 'z', 'x'])) == "PASSED"

def test1():
  assert driver(['a', 'b', 'c'], set(['b', 'c', 'a'])) == "PASSED"

def test2():
  assert driver(['z', 'd', 'e'], set(['e', 'z', 'd'])) == "PASSED"

