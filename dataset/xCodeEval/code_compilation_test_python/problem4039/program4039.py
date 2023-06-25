def program4039():
    k = input()
    r,i,j,o,t=0,-2,2*k,0,0
    f = lambda x,y: x*x+3*y*y>4*k*k
    while j>=0:    
        if (f(i,j) or f(i+1,j-1)): j-=2; continue
        r+=j*t
        i+=3;    
        if j&1: j+=5
        else: j+=3
        if t<2: t+=1    
    print r