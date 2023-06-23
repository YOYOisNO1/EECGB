    __author__ = 'vasiliy.lomanov'
    
    src = input().split()
    
    a = float(src[0])
    b = float(src[1])
    c = float(src[2])
    d = float(src[3])
    
    
def Euclid(a, b):
        q = a/b
        r = a - q*b
        if r == 0:
            return b
        else:
            return Euclid(b, r)
    
    
    k = min(b/d, a/c)
    
    if b/d < a/c:
        x = a*d
        y = a*d-c*b
    else:
        x = c*b
        y = c*b - a*d
    
    
    nod = Euclid(x, y)
    print str( int(y/nod) ) + "/" + str( int(x/nod) )