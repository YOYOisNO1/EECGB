def program6610():
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    mist2=n*2
    mist4=n
    otn=10
    for i in range(k)  :
        otn=min(mist4,l[i]//4)
        mist4-=otn
        l[i]-=otn*4
    
    mist2+=mist4
    for i in range(k)  :
        otn=min(mist2,l[i]//2)
        mist2-=otn
        l[i]-=otn*2
        
    mist4+=mist2
    
    mist4-=sum(l)
    
    if mist4>=0 :
        print("YES")
    else :
        print("NO")