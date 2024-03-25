from program321 import driver
def test0():
  assert driver("111111", "12345654321") == "PASSED"

def test1():
  assert driver("1111", "1234321") == "PASSED"

def test2():
  assert driver("13333122222", "123456789101110987654321") == "PASSED"

