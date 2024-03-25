from program676 import driver
def test0():
  assert driver("**//Google Android// - 12. ", "GoogleAndroid12") == "PASSED"

def test1():
  assert driver("****//Google Flutter//*** - 36. ", "GoogleFlutter36") == "PASSED"

def test2():
  assert driver("**//Google Firebase// - 478. ", "GoogleFirebase478") == "PASSED"

