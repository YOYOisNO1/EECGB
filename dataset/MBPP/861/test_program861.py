from program861 import driver
def test0():
  assert driver(["bcda", "abce", "cbda", "cbea", "adcb"], "abcd", ["bcda", "cbda", "adcb"]) == "PASSED"

def test1():
  assert driver(["recitals", " python"], "articles", ["recitals"]) == "PASSED"

def test2():
  assert driver([" keep", " abcdef", " xyz"], " peek", [" keep"]) == "PASSED"

