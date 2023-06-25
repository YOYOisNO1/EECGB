from ..program128 import program128
def test20():
    assert program128(27) == ['6\r\n1 2 3 4 5 12', '6\r\n2 3 4 5 6 7', '6\n1 2 3 4 5 12']