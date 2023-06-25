    from math import fmod
    
    
def pow1(x, base):
        if base == 0:
            return 1
        sq = pow1(x, base // 2)
        sq = (sq * sq) % m
    
        if base % 2:
            sq *= x
        return sq
    
    
def sum_pow(r, n):
        return (1 + fmod(-pow1(r, n + 1), m)) / (1 + fmod(- r, m))
    
    
    n, m = map(int, input().split())
    if n == 1:
        print(2 % m)
    else:
        print(int((2 * (sum_pow(3, n - 1))) % m))