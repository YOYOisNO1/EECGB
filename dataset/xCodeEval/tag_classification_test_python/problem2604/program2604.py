def program2604():
    from math import *
    from fractions import *
    
    p=int(input())
    
    s=sum([gcd(x,p-1)==1 for x in range(1,p)])
            
    print(s)