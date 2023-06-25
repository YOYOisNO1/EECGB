def f(l):
        n,m = l
        ms  = (n+1)//2
        ds  = ((ms+m-1)//m)*m
        return -1 if ds>n else ds
     
    l = list(map(int,input().split()))
    print(f(l))