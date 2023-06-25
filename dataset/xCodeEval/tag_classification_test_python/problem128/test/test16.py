from ..program128 import program128
def test16():
    assert program128(16) == ['5\r\n1 2 3 4 6', '5\n1 2 3 4 6']