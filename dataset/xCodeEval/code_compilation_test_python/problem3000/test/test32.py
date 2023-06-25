from ..program3000 import program3000
def test32():
    assert program3000(7 7
2C 3C 4C 2D 3D 4D JC
5C 6C 7C 5D 6D 7D QC
8C 9C TC 8D 9D TD KC
2H 3H 4H 2S 3S 4S AC
5H 6H 7H 5S 6S 7S KH
8H 9H TH 8S 9S TS AH
JD QD KD AD JH QH AS) == ['Solution exists.\nThere are no jokers.\nPut the first square to (1, 1).\nPut the second square to (1, 4).', 'Solution exists.\r\nThere are no jokers.\r\nPut the first square to (1, 1).\r\nPut the second square to (1, 4).']