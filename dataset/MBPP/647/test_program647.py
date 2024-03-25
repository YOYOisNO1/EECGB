from program647 import driver
def test0():
  assert driver("PythonProgramLanguage", ["Python", "Program", "Language"]) == "PASSED"

def test1():
  assert driver("PythonProgram", ["Python", "Program"]) == "PASSED"

def test2():
  assert driver("ProgrammingLanguage", ["Programming", "Language"]) == "PASSED"

