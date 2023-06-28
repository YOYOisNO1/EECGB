from program411 import driver
def test0():
  assert driver("android_tv", "AndroidTv") == "PASSED"

def test1():
  assert driver("google_pixel", "GooglePixel") == "PASSED"

def test2():
  assert driver("apple_watch", "AppleWatch") == "PASSED"

