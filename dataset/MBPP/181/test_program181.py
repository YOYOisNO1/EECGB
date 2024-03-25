from program181 import driver
def test0():
  assert driver(["tablets", "tables", "taxi", "tamarind"], 4, "ta") == "FAILED"

def test1():
  assert driver(["apples", "ape", "april"], 3, "ap") == "FAILED"

def test2():
  assert driver(["teens", "teenager", "teenmar"], 3, "teen") == "FAILED"

