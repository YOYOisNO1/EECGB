from program833 import driver
def test0():
  assert driver({1: "python", 2: "java"}, [1, 2]) == "PASSED"

def test1():
  assert driver({10: "red", 20: "blue", 30: "black"}, [10, 20, 30]) == "PASSED"

def test2():
  assert driver({27: "language", 39: "java", 44: "little"}, [27, 39, 44]) == "PASSED"

