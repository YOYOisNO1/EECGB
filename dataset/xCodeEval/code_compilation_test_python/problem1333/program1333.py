def program1333():
    n=int(input())
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    c=[0]*(n+1)
    ans=0
    for i in l:
        #print(i-1)
        c[i-1]+=1
    for i in l1:
        c[i-1]-=1
    
    for i in range(6):
        if c[i-1]%2:
            print(-1)
            break
        ans+=abs(c[i-1])//2
    else:print(ans//2)
        
        