from program87 import driver
def test0():
  assert driver({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"}, {"O": "Orange", "W": "White", "B": "Black"}, {"B": "Black", "R": "Red", "P": "Pink", "G": "Green", "W": "White", "O": "Orange"}) == "PASSED"

def test1():
  assert driver({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"}, {"L": "lavender", "B": "Blue"}, {"W": "White", "P": "Pink", "B": "Black", "R": "Red", "G": "Green", "L": "lavender"}) == "PASSED"

def test2():
  assert driver({"R": "Red", "B": "Black", "P": "Pink"}, {"L": "lavender", "B": "Blue"}, {"G": "Green", "W": "White"}, {"B": "Black", "P": "Pink", "R": "Red", "G": "Green", "L": "lavender", "W": "White"}) == "PASSED"

