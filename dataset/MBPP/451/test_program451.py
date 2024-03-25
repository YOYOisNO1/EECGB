from program451 import driver
def test0():
  assert driver(" Google    Flutter ", "GoogleFlutter") == "PASSED"

def test1():
  assert driver(" Google    Dart ", "GoogleDart") == "PASSED"

def test2():
  assert driver(" iOS    Swift ", "iOSSwift") == "PASSED"

