    import math
    n = input()
def solve(n):
        if n == 1:
            return 0
        k = (n-2)/3+1
        r = n%3
        k2 = int(math.ceil(math.sqrt(2*n/3)))
        while 3*k2**2 + k2 > 2*n:
            k2-=1
        if 3*k2**2 + k2 < 2*n:
            k2+=1
        #print k2
        if r==0:
            r2 = 3
        elif r==1:
            r2 = 2
        elif r2 == 2:
            r2 = 1
        return (k2-r2)/3+1
    
            
    print solve(n)