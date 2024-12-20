import sys
sys.path.append('../')
from program_19 import sort_numbers
def test_1():
    assert sort_numbers('') == ''
def test_2():
    assert sort_numbers('three') == 'three'
def test_3():
    assert sort_numbers('three five nine') == 'three five nine'
def test_4():
    assert sort_numbers('five zero four seven nine eight') == 'zero four five seven eight nine'
def test_5():
    assert sort_numbers('six five four three two one zero') == 'zero one two three four five six'