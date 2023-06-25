from ..program3004 import program3004
def test34():
    assert program3004(7 7
2C 3C 4C 2D 3D 4D JC
5C 6C J2 5D 6D 7D QC
8C 9C TC 8D 9D TD KC
2H 3H 4H 2S 3S 4S AC
5H 6H 7H 5S 6S 7S KH
8H 9H TH 8S 9S TS AH
JD QD KD AD JH QH AS) == ['Solution exists.\r\nReplace J2 with QS.\r\nPut the first square to (1, 1).\r\nPut the second square to (1, 4).', 'Solution exists.\nReplace J2 with 7C.\nPut the first square to (1, 4).\nPut the second square to (3, 1).', 'Solution exists.\r\nReplace J2 with 7C.\r\nPut the first square to (1, 1).\r\nPut the second square to (1, 4).']