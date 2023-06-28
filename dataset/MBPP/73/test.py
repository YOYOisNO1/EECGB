from program73 import driver
def test0():
  assert driver("Forces of the \ndarkness*are coming into the play.", ["Forces of the ", "darkness", "are coming into the play."]) == "PASSED"

def test1():
  assert driver("Mi Box runs on the \n Latest android*which has google assistance and chromecast.", ["Mi Box runs on the ", " Latest android", "which has google assistance and chromecast."]) == "PASSED"

def test2():
  assert driver("Certain services\nare subjected to change*over the seperate subscriptions.", ["Certain services", "are subjected to change", "over the seperate subscriptions."]) == "PASSED"

