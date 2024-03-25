from program621 import driver
def test0():
  assert driver(["MSM", "234", "is", "98", "123", "best", "4"], 6, ["MSM", "240", "is", "104", "129", "best", "10"]) == "PASSED"

def test1():
  assert driver(["Dart", "356", "is", "88", "169", "Super", "6"], 12, ["Dart", "368", "is", "100", "181", "Super", "18"]) == "PASSED"

def test2():
  assert driver(["Flutter", "451", "is", "44", "96", "Magnificent", "12"], 33, ["Flutter", "484", "is", "77", "129", "Magnificent", "45"]) == "PASSED"

