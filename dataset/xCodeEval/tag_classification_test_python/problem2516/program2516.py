def program2516():
    n,k=map(int,input().split())
    dict={}
    rem=10**9+7
    for i in range(1,n+1):
        dict[i]=[]
    for i in range(1,n+1):
        j=i
        while(j>0):
            if i%j==0:
                dict[i].append(j)
            j-=1
    arr=[[0 for i in range(n+1)] for j in range(k+1)]
    for i in range(1,n+1):
        arr[1][i]=1
    for i in range(2,k+1):
        for j in range(1,n+1):
            s=0
            for p in dict[j]:
                s=(s+arr[i-1][p])%rem
            arr[i][j]=s%rem
    
    
    #print(arr)
    s=0
    for i in range(1,n+1):
        s=(s+arr[k][i])%rem
    print(s%(10**9+7))