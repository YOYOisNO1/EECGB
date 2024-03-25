from program417 import driver
def test0():
  assert driver([['x', 'y'], ['x', 'z'], ['w', 't']], [['x', 'y', 'z'], ['w', 't']]) == "FAILED"

def test1():
  assert driver([['a', 'b'], ['a', 'c'], ['d', 'e']], [['a', 'b', 'c'], ['d', 'e']]) == "FAILED"

def test2():
  assert driver([['f', 'g'], ['f', 'g'], ['h', 'i']], [['f', 'g', 'g'], ['h', 'i']]) == "FAILED"

