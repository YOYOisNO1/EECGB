    
def gcd(x,y) :
        if y == 0 :
            return x
        else :
            t = x%y
            x = y
            y = t
            return gcd(x,y)
    
    x,y,a,b = map(int,input().split())
    k = x*y/gcd(x,y)
    
    t = a%k
    d,u = 0,0
    if t == 0 :
        d = a/k
    else :
        d = a/k + 1
    
    t = b%k
    if t == 0 :
        u = b/k
    else :
        u = b/k + 1
    
    res = u-d+1
    if res < 0
        res = 0
    
    print res