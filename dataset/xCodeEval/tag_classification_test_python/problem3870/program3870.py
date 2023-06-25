def program3870():
    n=int(input())
    a=[0] + [int(i) for i in input().split()] + [1001]
    ans=0
    if n==1:
        print(0)
    
    else:
        t=0
        for i in range(1,n+1):
            if a[i+1]-a[i-1]==2:
                t+=1
            else:
                ans=max(ans,t)
                t=0
    
        ans=max(ans,t)
    
        print(ans)