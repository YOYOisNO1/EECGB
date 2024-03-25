from program427 import driver
def test0():
  assert driver("2026-01-02", "02-01-2026") == "PASSED"

def test1():
  assert driver("2020-11-13", "13-11-2020") == "PASSED"

def test2():
  assert driver("2021-04-26", "26-04-2021") == "PASSED"

