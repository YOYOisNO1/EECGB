from program433 import driver
def test0():
  assert driver([1, 2, 3, 4, 5], 4, "No, entered number is less than those in the array") == "PASSED"

def test1():
  assert driver([2, 3, 4, 5, 6], 8, "Yes, the entered number is greater than those in the array") == "PASSED"

def test2():
  assert driver([9, 7, 4, 8, 6, 1], 11, "Yes, the entered number is greater than those in the array") == "PASSED"

