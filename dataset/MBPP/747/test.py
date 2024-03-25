from program747 import driver
def test0():
  assert driver("AGGT12", "12TXAYB", "12XBA", 6, 7, 5, 2) == "PASSED"

def test1():
  assert driver("Reels", "Reelsfor", "ReelsforReels", 5, 8, 13, 5) == "PASSED"

def test2():
  assert driver("abcd1e2", "bc12ea", "bd1ea", 7, 6, 5, 3) == "PASSED"

