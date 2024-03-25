from program419 import driver
def test0():
  assert driver([22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5], 243) == "PASSED"

def test1():
  assert driver([5.0, 2.0, 9.0, 24.3, 29.0], 345) == "PASSED"

def test2():
  assert driver([25.0, 56.7, 89.2], 513) == "PASSED"

