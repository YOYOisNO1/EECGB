def program3474():
    n,m=map(int,input().split())
    lst=[0]*m
    for i in range(1,m+1):
        lst[i*i%m]+=(n-i)//m+1
    print(sum(x*lst[-i] for i,x in enumerate(lst)))