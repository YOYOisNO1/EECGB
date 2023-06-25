def program5085():
    # 
    
    n,k=map(int, input().split())
    
    a=list(map(int, input().split()))
    
    b=[0]*k
    max=0
    
    for i in range(k):
        for j in range(n):
            if (j+1)%k==i: continue
            b[i]=b[i]+a[j]
        if b[i]<0: b[i]=-b[i]
        if i==0: max=b[0]
        if b[i]>max: max=b[i]
    
    print(max)