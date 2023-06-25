def program703():
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    li=[0]*(n+1)
    for i in l:
        for j in range(i,n+1):
            if li[j]==0:
                li[j]=i
    for i in range(1,n+1):
        print(li[i],end=" ")