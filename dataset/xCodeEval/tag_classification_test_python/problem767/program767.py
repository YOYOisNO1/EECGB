def program767():
    n,m=map(int,input().split())
    p=n//m
    count=0
    while p>0:
        count=n
        n+=p
        p=(n//m-count//m)
    print(n)