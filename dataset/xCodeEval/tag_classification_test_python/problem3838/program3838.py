def program3838():
    from fractions import Fraction
    best_play = int(max(input().split(), key=int))
    chances = sum(1 for _ in range(best_play, 7))
    res = Fraction(chances, 6)
    print("{}/{}".format(res.numerator, res.denominator))