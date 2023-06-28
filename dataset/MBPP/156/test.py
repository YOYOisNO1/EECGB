from program156 import driver
def test0():
  assert driver([["333", "33"], ["1416", "55"]], [[333, 33], [1416, 55]]) == "FAILED"

def test1():
  assert driver([["999", "99"], ["1000", "500"]], [[999, 99], [1000, 500]]) == "FAILED"

def test2():
  assert driver([["666", "66"], ["1500", "555"]], [[666, 66], [1500, 555]]) == "FAILED"

