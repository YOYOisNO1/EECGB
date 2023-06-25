def program1708():
    n,m=map(int,input().split())
    if m==0:
        print(1)
    elif n==m:
        print(0)
    elif m>n//2:
        print(n-m)
    else:
        print(m)