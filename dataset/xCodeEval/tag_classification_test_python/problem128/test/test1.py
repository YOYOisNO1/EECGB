from ..program128 import program128
def test1():
    assert program128(9) == ['3\n1 2 6', '3\r\n1 2 6', '3\r\n2 3 4']