import sys
sys.path.append('../')
from program_78 import hex_key
def test_1():
    assert hex_key("AB") == 1, "First test error: " + str(hex_key("AB"))      
def test_2():
    assert hex_key("1077E") == 2, "Second test error: " + str(hex_key("1077E"))  
def test_3():
    assert hex_key("ABED1A33") == 4, "Third test error: " + str(hex_key("ABED1A33"))      
def test_4():
    assert hex_key("2020") == 2, "Fourth test error: " + str(hex_key("2020"))  
def test_5():
    assert hex_key("123456789ABCDEF0") == 6, "Fifth test error: " + str(hex_key("123456789ABCDEF0"))      
def test_6():
    assert hex_key("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(hex_key("112233445566778899AABBCCDDEEFF00"))  
def test_7():
    assert hex_key([]) == 0