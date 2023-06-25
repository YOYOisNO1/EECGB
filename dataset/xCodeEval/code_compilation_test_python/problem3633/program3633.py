    # area of equilater triangle s**2 * sqrt(3) / 4
    from math import sqrt
    
    answers = {}
    
def solve(s1, s2, s3, y, ite):
        if s1 == y and s2 == y and s3 == y:
            return ite
        if (s1, s2, s3, y) in answers.keys():
            return answers[(s1, s2, s3, y)]
        big = max(max(s1, s2), s3)
        small = min(min(s1, s2), s3)
        other = s1+s2+s3-big-small
        rest = other-small
        new = max(rest+1, y)
        bigg = max(big-1, y)
        ite_min = 300000
        if new == y and bigg == y:
            return solve(small, other, new, y, ite+1)
        for i in range(new, bigg):
            ite_min = min(ite_min, solve(small, other, i, y, 0))
        answers[(s1, s2, s3, y)] = ite_min + ite + 1
        return ite_min + ite + 1
    
    x, y = [int(i) for i in input().split()]
    print(solve(x, x, x, y, 0))
    
    
    