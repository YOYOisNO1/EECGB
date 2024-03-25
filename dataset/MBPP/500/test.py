from program500 import driver
def test0():
  assert driver(["hello", "there", "have", "a", "rocky", "day"], "  hello there have a rocky day") == "PASSED"

def test1():
  assert driver(["Hi", "there", "How", "are", "you"], "  Hi there How are you") == "PASSED"

def test2():
  assert driver(["Part", "of", "the", "journey", "is", "end"], "  Part of the journey is end") == "PASSED"

