from program857 import driver
def test0():
  assert driver(["Red", "Blue", "Black", "White", "Pink"], [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]) == "PASSED"

def test1():
  assert driver(["python"], [['p', 'y', 't', 'h', 'o', 'n']]) == "PASSED"

def test2():
  assert driver([" red ", "green", " black", "blue ", " orange", "brown"], [[' ', 'r', 'e', 'd', ' '], ['g', 'r', 'e', 'e', 'n'], [' ', 'b', 'l', 'a', 'c', 'k'], ['b', 'l', 'u', 'e', ' '], [' ', 'o', 'r', 'a', 'n', 'g', 'e'], ['b', 'r', 'o', 'w', 'n']]) == "PASSED"

