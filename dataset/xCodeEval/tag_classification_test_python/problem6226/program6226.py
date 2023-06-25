    from math import gcd
    import sys
    t=1
def inp(): return sys.stdin.readline().strip()
    
def lcm(a, b):
        return abs(a*b) // gcd(a, b)
        
        
    for _ in range(t):
        a, b=map(int, inp().split())
        period= lcm(a,b)
        d=period//a
        m=period//b
        if(a>b):
            m-=1
        else:
            d-=1
        if d>m:
            print('Dasha')
        elif d<m:
            print('Masha')
        else:
            print('Equal')
            
        
        
        
            
            