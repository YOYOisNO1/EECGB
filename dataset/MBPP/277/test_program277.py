from program277 import driver
def test0():
  assert driver({"Cierra Vega": 175, "Alden Cantrell": 180, "Kierra Gentry": 165, "Pierre Cox": 190}, 170, {"Cierra Vega": 175, "Alden Cantrell": 180, "Pierre Cox": 190}) == "PASSED"

def test1():
  assert driver({"Cierra Vega": 175, "Alden Cantrell": 180, "Kierra Gentry": 165, "Pierre Cox": 190}, 180, {"Alden Cantrell": 180, "Pierre Cox": 190}) == "PASSED"

def test2():
  assert driver({"Cierra Vega": 175, "Alden Cantrell": 180, "Kierra Gentry": 165, "Pierre Cox": 190}, 190, {"Pierre Cox": 190}) == "PASSED"

