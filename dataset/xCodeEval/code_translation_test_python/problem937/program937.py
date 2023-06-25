def program937():
    n,k = map(int,input().split())
    if k==1:
        print(n)
    else:
        x = str(bin(n))
        x = x[2:]
        ans = len(x)
        print(2**ans-1)