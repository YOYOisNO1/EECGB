def program3221():
    from math import *
    from fractions import *
    
    p=int(input())
    
    s = 0
    for x in range(1,p):
        if(gcd(x,p-1)==1):
            s+=1
    print s