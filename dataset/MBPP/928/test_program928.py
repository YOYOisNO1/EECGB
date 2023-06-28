from program928 import driver
def test0():
  assert driver("2026-01-02", "02-01-2026") == "PASSED"

def test1():
  assert driver("2021-01-04", "04-01-2021") == "PASSED"

def test2():
  assert driver("2030-06-06", "06-06-2030") == "PASSED"

