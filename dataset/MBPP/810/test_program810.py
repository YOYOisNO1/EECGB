from program810 import driver
def test0():
  assert driver(4, 2, 0, -2, ['p', 'p', 'p', 'p', 'q', 'q']) == "PASSED"

def test1():
  assert driver(0, 1, 2, 3, ['q', 'r', 'r', 's', 's', 's']) == "PASSED"

def test2():
  assert driver(11, 15, 12, 23, ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's']) == "PASSED"

