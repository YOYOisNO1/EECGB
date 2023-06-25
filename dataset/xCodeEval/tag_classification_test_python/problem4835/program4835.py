def program4835():
    n=int(input())
    
    l=[]
    
    for i in range(n):
        m=list(map(int,input().split()))
        l.append(m)
    
    ans=0
    
    for i in range(n):
        ans+=l[i][i]
        l[i][i]=0
    j=n-1
    for i in range(n):
        ans+=l[i][j]
        l[i][j]=0
        j-=1
    j=n//2
    for i in range(n):
        ans+=l[i][j]
        l[i][j]=0
    
    for i in range(n):
        ans+=l[j][i]
    
    print(ans)