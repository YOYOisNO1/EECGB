from program464 import driver
def test0():
  assert driver({"Cierra Vega": 12, "Alden Cantrell": 12, "Kierra Gentry": 12, "Pierre Cox": 12}, 10, False) == "PASSED"

def test1():
  assert driver({"Cierra Vega": 12, "Alden Cantrell": 12, "Kierra Gentry": 12, "Pierre Cox": 12}, 12, True) == "PASSED"

def test2():
  assert driver({"Cierra Vega": 12, "Alden Cantrell": 12, "Kierra Gentry": 12, "Pierre Cox": 12}, 5, False) == "PASSED"

