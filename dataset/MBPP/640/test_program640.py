from program640 import driver
def test0():
  assert driver(["python (chrome)"], "python") == "PASSED"

def test1():
  assert driver(["string(.abc)"], "string") == "PASSED"

def test2():
  assert driver(["alpha(num)"], "alpha") == "PASSED"

