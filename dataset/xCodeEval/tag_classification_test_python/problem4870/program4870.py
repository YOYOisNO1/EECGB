def program4870():
    n,a,b=map(int,input().split())
    x=list(map(int,input().split()))
    s=0
    for i in range(n):
        if x[i]!=2 and x[n-i-1]!=2 and x[i]!=x[n-i-1]:
            exit(print(-1))
        if x[i]==2 and x[n-1-i]==0:
            s+=a
        elif x[i]==2 and x[n-1-i]==1:
            s+=b
        elif x[i]==2 and x[n-1-i]==2: 
            s+=min(a,b)
    print(s)
    
            