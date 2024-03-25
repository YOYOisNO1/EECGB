from program27 import driver
def test0():
  assert driver(["4words", "3letters", "4digits"], ["words", "letters", "digits"]) == "PASSED"

def test1():
  assert driver(["28Jan", "12Jan", "11Jan"], ["Jan", "Jan", "Jan"]) == "PASSED"

def test2():
  assert driver(["wonder1", "wonder2", "wonder3"], ["wonder", "wonder", "wonder"]) == "PASSED"

