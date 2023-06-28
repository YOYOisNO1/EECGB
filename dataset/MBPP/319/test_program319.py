from program319 import driver
def test0():
  assert driver("Please move back to strem", ["strem"]) == "PASSED"

def test1():
  assert driver("4K Ultra HD streaming player", ["Ultra"]) == "PASSED"

def test2():
  assert driver("Streaming Media Player", ["Media"]) == "PASSED"

