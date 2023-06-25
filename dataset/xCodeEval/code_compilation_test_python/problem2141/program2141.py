def program2141():
    from math import *
    
    n = int(input()) * 2
    
    k = int(round(sqrt(n)))
    
    found = False
    
    i = 1
    while i < k
        r = n - i * i - i
        i += 1
        x = int(floor(sqrt(r)))
        if x * (x + 1) == r:
            found = True
            break
    
    print("YES") if found else "NO"