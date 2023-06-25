def program3834():
    a,b,c,n= list(map(int, input().split() ) )
    nreal= a+b-c
    if c>a or c>b or a>n or b>n or c>n:
        print(-1)
    elif n-nreal>=1:
        print(n-nreal)
    else:
        print(-1)