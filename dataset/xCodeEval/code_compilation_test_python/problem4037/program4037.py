def program4037():
    k = input()
    r = 0
    i,j=0,k
    f = lambda x,y: x*x+3*y*y>4*k*k
    while j>=0:
        o = i&1
        while j>=0:
            j-=1
            x,y = 3*i+1,2*j-1+o        
            if f(x,y): continue
            if f(x+1,y-1): continue
            break
        if j<0: break    
        r += (2*j+o-1)*(2 if i else 1)
        i,j=i+1,j+2
    print r