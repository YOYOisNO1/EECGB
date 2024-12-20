import sys
sys.path.append('../')
from program_41 import car_race_collision
def test_1():
    assert car_race_collision(2) == 4
def test_2():
    assert car_race_collision(3) == 9
def test_3():
    assert car_race_collision(4) == 16
def test_4():
    assert car_race_collision(8) == 64
def test_5():
    assert car_race_collision(10) == 100