from program829 import driver
def test0():
  assert driver(["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"], "bbb") == "PASSED"

def test1():
  assert driver(["abc", "bcd", "abc", "bcd", "bcd", "bcd"], "abc") == "PASSED"

def test2():
  assert driver(["cdma", "gsm", "hspa", "gsm", "cdma", "cdma"], "gsm") == "PASSED"

