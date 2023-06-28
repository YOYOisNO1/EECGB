from program206 import driver
def test0():
  assert driver(["DSP ", "IS ", "BEST ", "FOR ", "ALL ", "UTS"], ["DSP IS ", "IS BEST ", "BEST FOR ", "FOR ALL ", "ALL UTS"]) == "FAILED"

def test1():
  assert driver(["RES ", "IS ", "BEST ", "FOR ", "ALL ", "QESR"], ["RES IS ", "IS BEST ", "BEST FOR ", "FOR ALL ", "ALL QESR"]) == "FAILED"

def test2():
  assert driver(["MSAM", "IS ", "BEST ", "FOR ", "ALL ", "SKD"], ["MSAMIS ", "IS BEST ", "BEST FOR ", "FOR ALL ", "ALL SKD"]) == "FAILED"

