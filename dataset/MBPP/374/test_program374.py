from program374 import driver
def test0():
  assert driver("ab", ["ab", "ba"]) == "PASSED"

def test1():
  assert driver("abc", ["abc", "bac", "bca", "acb", "cab", "cba"]) == "PASSED"

def test2():
  assert driver("abcd", ["abcd", "bacd", "bcad", "bcda", "acbd", "cabd", "cbad", "cbda", "acdb", "cadb", "cdab", "cdba", "abdc", "badc", "bdac", "bdca", "adbc", "dabc", "dbac", "dbca", "adcb", "dacb", "dcab", "dcba"]) == "PASSED"

