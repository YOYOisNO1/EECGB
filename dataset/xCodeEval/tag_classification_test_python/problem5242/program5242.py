def program5242():
    r=lambda:map(int,input().split())
    n,m=r()
    
    d=[0,0,0,0,0]
    D=[0,0,0,0,0]
    
    
    for i in range(1,n+1):
        d[i%5]+=1
    for j in range(1,m+1):
        D[j%5]+=1
    #print(d,D)
    R=0
    for i in range(1,5):
        R+=d[i]*D[-i]
    R+=d[0]*D[0]
    print(R)