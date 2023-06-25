    import math
    
def f(n):
        c = 0
        for i in range(2,n):
            for j in range(i,n):
                s = i*i+j*j
                r = int(math.sqrt(s))
                if r*r == s and r<=n:
                    c+=1
        return c
    
    n = int(input())  #1e4
    print(f(n))