from program965 import driver
def test0():
  assert driver("PythonProgram", "python_program") == "PASSED"

def test1():
  assert driver("pythonLanguage", "python_language") == "PASSED"

def test2():
  assert driver("ProgrammingLanguage", "programming_language") == "PASSED"

