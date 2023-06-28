from program727 import driver
def test0():
  assert driver("123abcjw:, .@! eiw", "123abcjweiw") == "PASSED"

def test1():
  assert driver("Hello1234:, ! Howare33u", "Hello1234Howare33u") == "PASSED"

def test2():
  assert driver("Cool543Triks@:, Make@987Trips", "Cool543TriksMake987Trips") == "PASSED"

