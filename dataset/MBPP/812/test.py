from program812 import driver
def test0():
  assert driver("ravipadu Road", "ravipadu Rd.") == "PASSED"

def test1():
  assert driver("palnadu Road", "palnadu Rd.") == "PASSED"

def test2():
  assert driver("eshwar enclave Road", "eshwar enclave Rd.") == "PASSED"

