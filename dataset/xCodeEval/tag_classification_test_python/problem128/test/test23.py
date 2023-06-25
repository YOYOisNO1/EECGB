from ..program128 import program128
def test23():
    assert program128(35) == ['7\r\n2 3 4 5 6 7 8', '7\r\n1 2 3 4 5 6 14', '7\n1 2 3 4 5 6 14']