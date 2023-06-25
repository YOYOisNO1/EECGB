    from collections import defaultdict
    import sys
    from itertools import *
    sys.setrecursionlimit(999999999)
    
    n,c = map(int,input().split())
    
    P = 10**6+3
    fak= [1]*P
    
    for i in xrange(P-1):
        fak[i+1]= (fak[i]*(i+1))%P
        
    
    
def pow(q,w):
        if w==0:
            return 1
        pom = pow(q,w/2)
        h = 1
        if w%2:
            h = q
        return (((pom*pom)%P)*h)%P
    
def inv(q):
        return pow(q,P-2)
    
    ans = -1
    i=n
    ans+= (fak[n+c]* inv(fak[n])*inv(fak[c]))%P
    
    print(ans)