    import sys
    from fractions import Fraction
    
def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def rinput():   return map(int, sys.stdin.readline().strip().split()) 
def get_list(): return list(map(int, sys.stdin.readline().strip().split())) 
    mod = int(1e9)+7
    
    x, y, n = rinput()
    ans = Fraction(x, y).limit_denominator(n)
    print(str(ans.numerator)+'/'+str(ans.denominator))