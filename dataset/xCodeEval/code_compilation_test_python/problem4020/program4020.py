def program4020():
    from math import *
    
    n=input()
    m = 120000
    x=[]
    for i in range(m):
        x.append(True)
    
    for i in range(2,int(sqrt(m))):
        if x[i]:
            for k in range(2*i, m, i):
    
                x[k] = False
    
    x[0] = False
    x[1] = False
    
    y=[]
    for i in range(m):
        r = int(str(i)[::-1])
        if x[i] and r < m and x[r] and r!=i:
            y.append(i)
    
    print y[n-1]