from program7 import driver
def test0():
  assert driver("Please move back to stream", ["Please", "move", "back", "stream"]) == "PASSED"

def test1():
  assert driver("Jing Eco and Tech", ["Jing", "Tech"]) == "PASSED"

def test2():
  assert driver("Jhingai wulu road Zone 3", ["Jhingai", "wulu", "road", "Zone"]) == "PASSED"

