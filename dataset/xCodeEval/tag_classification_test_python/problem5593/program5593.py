def program5593():
    n=int(input())
    l=[[0 if i!=0 else 1 for i in range(n)] if k!=0 else [1]*n for k in range(n)]
    for i in range(1,n):
        for k in range(1,n):
            l[i][k]=l[i-1][k]+l[i][k-1]
    print(l[-1][-1])