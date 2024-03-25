from program864 import driver
def test0():
  assert driver(["php", "res", "Python", "abcd", "Java", "aaa"], ["php", "aaa"]) == "PASSED"

def test1():
  assert driver(["abcd", "Python", "abba", "aba"], ["abba", "aba"]) == "PASSED"

def test2():
  assert driver(["abcd", "abbccbba", "abba", "aba"], ["abbccbba", "abba", "aba"]) == "PASSED"

