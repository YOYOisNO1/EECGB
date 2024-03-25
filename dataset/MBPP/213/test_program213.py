from program213 import driver
def test0():
  assert driver(["Manjeet", "Nikhil", "Akshat"], [" Singh", " Meherwal", " Garg"], ["Manjeet Singh", "Nikhil Meherwal", "Akshat Garg"]) == "FAILED"

def test1():
  assert driver(["Shaik", "Ayesha", "Sanya"], [" Dawood", " Begum", " Singh"], ["Shaik Dawood", "Ayesha Begum", "Sanya Singh"]) == "FAILED"

def test2():
  assert driver(["Harpreet", "Priyanka", "Muskan"], ["Kour", " Agarwal", "Sethi"], ["HarpreetKour", "Priyanka Agarwal", "MuskanSethi"]) == "FAILED"

