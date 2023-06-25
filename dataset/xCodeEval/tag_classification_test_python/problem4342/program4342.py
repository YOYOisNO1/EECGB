    #!/usr/bin/env python3
    from fractions import gcd
    
def ri():
        return map(int, input().split())
    
    
    a, b = ri()
    c, d = ri()
    
    if c > a:
        a, c = c, a
        b, d = d, b
    
    for i in range(10**5):
        if b-d+i*a >=0 and (b-d+i*a)%c == 0:
            print(b+i*a)
            exit()
    else:
        print(-1)