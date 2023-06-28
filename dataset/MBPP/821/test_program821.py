from program821 import driver
def test0():
  assert driver({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"}, {"B": "Black", "R": "Red", "P": "Pink", "G": "Green", "W": "White"}) == "PASSED"

def test1():
  assert driver({"R": "Red", "B": "Black", "P": "Pink"}, {"O": "Orange", "W": "White", "B": "Black"}, {"O": "Orange", "P": "Pink", "B": "Black", "W": "White", "R": "Red"}) == "PASSED"

def test2():
  assert driver({"G": "Green", "W": "White"}, {"O": "Orange", "W": "White", "B": "Black"}, {"W": "White", "O": "Orange", "G": "Green", "B": "Black"}) == "PASSED"

