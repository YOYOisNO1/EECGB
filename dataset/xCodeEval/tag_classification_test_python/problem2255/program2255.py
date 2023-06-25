def program2255():
    a=int(input(''))
    b=list(map(int,input().split()))
    t=[]
    p=0
    l=0
    z=[]
    q=0
    k=0
    for i in range(a):
        if(not(b[p]==0)):
            t.append(b[p])
        p=p+1
    for jk in range(len(t)):
        if(not(t[l] in z)):
            z.append(t[l])
        l=l+1
    print(len(z))
    
    
    
    
    
    
    
    
            