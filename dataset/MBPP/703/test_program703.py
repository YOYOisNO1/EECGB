from program703 import driver
def test0():
  assert driver({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 5, True) == "PASSED"

def test1():
  assert driver({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 6, True) == "PASSED"

def test2():
  assert driver({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 10, False) == "PASSED"

