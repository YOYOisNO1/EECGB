import sys
sys.path.append('../')
from program_81 import numerical_letter_grade
def test_1():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
def test_2():
    assert numerical_letter_grade([1.2]) == ['D+']
def test_3():
    assert numerical_letter_grade([0.5]) == ['D-']
def test_4():
    assert numerical_letter_grade([0.0]) == ['E']
def test_5():
    assert numerical_letter_grade([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+']
def test_6():
    assert numerical_letter_grade([0, 0.7]) == ['E', 'D-']
def test_7():
    assert True