import sys
sys.path.append('../')
from program_157 import right_angle_triangle
def test_1():
    assert right_angle_triangle(3, 4, 5) == True, "This prints if this assert fails 1 (good for debugging!)"
def test_2():
    assert right_angle_triangle(1, 2, 3) == False
def test_3():
    assert right_angle_triangle(10, 6, 8) == True
def test_4():
    assert right_angle_triangle(2, 2, 2) == False
def test_5():
    assert right_angle_triangle(7, 24, 25) == True
def test_6():
    assert right_angle_triangle(10, 5, 7) == False
def test_7():
    assert right_angle_triangle(5, 12, 13) == True
def test_8():
    assert right_angle_triangle(15, 8, 17) == True
def test_9():
    assert right_angle_triangle(48, 55, 73) == True
def test_10():
    assert right_angle_triangle(1, 1, 1) == False, "This prints if this assert fails 2 (also good for debugging!)"
def test_11():
    assert right_angle_triangle(2, 2, 10) == False