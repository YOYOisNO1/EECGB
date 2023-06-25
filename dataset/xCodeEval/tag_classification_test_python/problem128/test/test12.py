from ..program128 import program128
def test12():
    assert program128(12) == ['4\n1 2 3 6', '4\r\n1 2 3 6', '4\r\n1 2 4 5']