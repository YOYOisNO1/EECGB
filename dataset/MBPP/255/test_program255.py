from program255 import driver
def test0():
  assert driver(["Red", "Green", "Blue"], 1, [["Red"], ["Green"], ["Blue"]]) == "FAILED"

def test1():
  assert driver(["Red", "Green", "Blue"], 2, [["Red", "Red"], ["Red", "Green"], ["Red", "Blue"], ["Green", "Green"], ["Green", "Blue"], ["Blue", "Blue"]]) == "FAILED"

def test2():
  assert driver(["Red", "Green", "Blue"], 3, [["Red", "Red", "Red"], ["Red", "Red", "Green"], ["Red", "Red", "Blue"], ["Red", "Green", "Green"], ["Red", "Green", "Blue"], ["Red", "Blue", "Blue"], ["Green", "Green", "Green"], ["Green", "Green", "Blue"], ["Green", "Blue", "Blue"], ["Blue", "Blue", "Blue"]]) == "FAILED"

