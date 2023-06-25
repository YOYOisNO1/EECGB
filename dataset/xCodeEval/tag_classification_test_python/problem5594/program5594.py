def program5594():
    n=int(input())
    a=[]
    for i in range(n):
        a.append([1]*n)
    
    for i in range(0, n-1):
            for j in range(n-1):
                a[i][j]=a[i-1][j]+a[i][j-1]
    
    print(max(max(a)))