from program102 import driver
def test0():
  assert driver("python_program", "PythonProgram") == "PASSED"

def test1():
  assert driver("python_language", "PythonLanguage") == "PASSED"

def test2():
  assert driver("programming_language", "ProgrammingLanguage") == "PASSED"

