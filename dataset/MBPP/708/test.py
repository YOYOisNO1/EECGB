from program708 import driver
def test0():
  assert driver("python program", ["python", "program"]) == "PASSED"

def test1():
  assert driver("Data Analysis", ["Data", "Analysis"]) == "PASSED"

def test2():
  assert driver("Hadoop Training", ["Hadoop", "Training"]) == "PASSED"

