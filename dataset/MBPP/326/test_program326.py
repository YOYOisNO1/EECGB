from program326 import driver
def test0():
  assert driver(["UTS is best for RTF", "RTF love UTS", "UTS is best"], "UTS") == "PASSED"

def test1():
  assert driver(["Its been a great year", "this year is so worse", "this year is okay"], "year") == "PASSED"

def test2():
  assert driver(["Families can be reunited", "people can be reunited", "Tasks can be achieved "], "can") == "PASSED"

