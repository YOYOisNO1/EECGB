from program725 import driver
def test0():
  assert driver("Cortex \"A53\" Based \"multi\" tasking \"Processor\"", ["A53", "multi", "Processor"]) == "PASSED"

def test1():
  assert driver("Cast your \"favorite\" entertainment \"apps\"", ["favorite", "apps"]) == "PASSED"

def test2():
  assert driver("Watch content \"4k Ultra HD\" resolution with \"HDR 10\" Support", ["4k Ultra HD", "HDR 10"]) == "PASSED"

