from program330 import driver
def test0():
  assert driver("For the four consumer complaints contact manager AKR reddy", ["For", "the", "four", "AKR", "reddy"]) == "PASSED"

def test1():
  assert driver("Certain service are subject to change MSR", ["are", "MSR"]) == "PASSED"

def test2():
  assert driver("Third party legal desclaimers", ["Third", "party", "legal"]) == "PASSED"

