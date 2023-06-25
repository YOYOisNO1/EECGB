from ..program3002 import program3002
def test35():
    assert program3002(7 7
2C 3C 4C 2D 3D 4D JC
5C 6C 7C 5D 6D 7D QC
8C 9C TC 8D J2 TD KC
2H 3H 4H J1 3S 4S AC
5H 6H 7H 5S 6S 7S KH
8H 9H TH 8S 9S TS AH
JD QD KD AD JH QH AS) == ['Solution exists.\r\nReplace J1 with 2S and J2 with 9D.\r\nPut the first square to (1, 1).\r\nPut the second square to (1, 4).', 'Solution exists.\nReplace J1 with 9D and J2 with 2S.\nPut the first square to (1, 1).\nPut the second square to (4, 1).', 'Solution exists.\r\nReplace J1 with 9D and J2 with 2S.\r\nPut the first square to (1, 1).\r\nPut the second square to (1, 5).']