def program3489():
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    
    i=0
    candy=0
    while k>0 and i<n :
        candy+=s[i]
        p = min(candy,8)
        k-=p
        i+=1
        candy-=p
    
    if k>0:
        print(-1)
        exit()
    print(i)