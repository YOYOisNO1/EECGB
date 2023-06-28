from program104 import driver
def test0():
  assert driver([["green", "orange"], ["black", "white"], ["white", "black", "orange"]], [["green", "orange"], ["black", "white"], ["black", "orange", "white"]]) == "PASSED"

def test1():
  assert driver([[" red ", "green"], ["blue ", " black"], [" orange", "brown"]], [[" red ", "green"], [" black", "blue "], [" orange", "brown"]]) == "PASSED"

def test2():
  assert driver([["zilver", "gold"], ["magnesium", "aluminium"], ["steel", "bronze"]], [["gold", "zilver"], ["aluminium", "magnesium"], ["bronze", "steel"]]) == "PASSED"

