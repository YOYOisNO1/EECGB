import sys
sys.path.append('../')
from program_162 import string_to_md5
def test_1():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
def test_2():
    assert string_to_md5('') == None
def test_3():
    assert string_to_md5('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'
def test_4():
    assert string_to_md5('password') == '5f4dcc3b5aa765d61d8327deb882cf99'
def test_5():
    assert True