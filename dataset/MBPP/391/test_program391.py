from program391 import driver
def test0():
  assert driver(["S001", "S002", "S003", "S004"], ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"], [85, 98, 89, 92], [{"S001": {"Adina Park": 85}}, {"S002": {"Leyton Marsh": 98}}, {"S003": {"Duncan Boyle": 89}}, {"S004": {"Saim Richards": 92}}]) == "PASSED"

def test1():
  assert driver(["abc", "def", "ghi", "jkl"], ["python", "program", "language", "programs"], [100, 200, 300, 400], [{"abc": {"python": 100}}, {"def": {"program": 200}}, {"ghi": {"language": 300}}, {"jkl": {"programs": 400}}]) == "PASSED"

def test2():
  assert driver(["A1", "A2", "A3", "A4"], ["java", "C", "C++", "DBMS"], [10, 20, 30, 40], [{"A1": {"java": 10}}, {"A2": {"C": 20}}, {"A3": {"C++": 30}}, {"A4": {"DBMS": 40}}]) == "PASSED"

