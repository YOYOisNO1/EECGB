def program1178():
    import numpy as np
    #yy
    n,c=map(int,input().split())
    p=list(map(int,input().split()))
    t=list(map(int,input().split()))
    pf=[]
    pr=[]
    x=0
    for i in range(n):
        x+=t[i]
        pf.append(max(0, p[i]-x*c))
    pf=np.array(pf)
    c1=sum(pf)
    
    
    p.reverse()
    t.reverse()
    x=0
    for i in range(n):
        x+=t[i]
        pr.append( max(0,p[i]-x*c))
        
    pr =np.array(pr)
    c2=sum(pr)
    
    if(c1>c2):
        print('Limak')
    elif(c1==c2):
        print('Tie')
    else:
        print('Radewoosh')
    
    
    