    a,b,x,y = [int(x) for x in input().split()]
    
def gcd(r,s):
        if (r == 0 or s == 0):
            return r+s
        else:
            if r > s:
                return gcd(r-s,s)
            else:
                return gcd(r,s-r)
    
    g = gcd(x,y)
    x1 = int(x/g)
    y1 = int(y/g)
    
    if (x1 <= a and y1 <=b):   
        c = 0
        while (x1*c <= a and y1*c<= b):
            c += 1
        print(x1*(c-1),y1*(c-1))
    else:
        print(0,0)