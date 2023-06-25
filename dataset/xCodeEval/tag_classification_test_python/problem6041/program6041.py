def program6041():
    l=lambda:map(int,input().split())
    n,k=l()
    s=bin(n)[2:]
    ls=len(s)
    if k==1:
        print(n)
    else:
        print(2**ls-1) 