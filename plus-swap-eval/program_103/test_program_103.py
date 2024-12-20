import sys
sys.path.append('../')
from program_103 import rounded_avg
def test_1():
    assert rounded_avg(1, 5) == "0b11"
def test_2():
    assert rounded_avg(7, 13) == "0b1010"
def test_3():
    assert rounded_avg(964,977) == "0b1111001010"
def test_4():
    assert rounded_avg(996,997) == "0b1111100100"
def test_5():
    assert rounded_avg(560,851) == "0b1011000010"
def test_6():
    assert rounded_avg(185,546) == "0b101101110"
def test_7():
    assert rounded_avg(362,496) == "0b110101101"
def test_8():
    assert rounded_avg(350,902) == "0b1001110010"
def test_9():
    assert rounded_avg(197,233) == "0b11010111"
def test_10():
    assert rounded_avg(7, 5) == -1
def test_11():
    assert rounded_avg(5, 1) == -1
def test_12():
    assert rounded_avg(5, 5) == "0b101"