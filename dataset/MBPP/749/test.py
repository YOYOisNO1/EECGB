from program749 import driver
def test0():
  assert driver(["4", "12", "45", "7", "0", "100", "200", "-12", "-500"], [-500, -12, 0, 4, 7, 12, 45, 100, 200]) == "PASSED"

def test1():
  assert driver(["2", "3", "8", "4", "7", "9", "8", "2", "6", "5", "1", "6", "1", "2", "3", "4", "6", "9", "1", "2"], [1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9, 9]) == "PASSED"

def test2():
  assert driver(["1", "3", "5", "7", "1", "3", "13", "15", "17", "5", "7 ", "9", "1", "11"], [1, 1, 1, 3, 3, 5, 5, 7, 7, 9, 11, 13, 15, 17]) == "PASSED"

