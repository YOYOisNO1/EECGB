from program826 import driver
def test0():
  assert driver(1, 2, 3, "Obtuse-angled Triangle") == "PASSED"

def test1():
  assert driver(2, 2, 2, "Acute-angled Triangle") == "PASSED"

def test2():
  assert driver(1, 0, 1, "Right-angled Triangle") == "PASSED"

