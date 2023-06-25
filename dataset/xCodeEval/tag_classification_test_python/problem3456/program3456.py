def program3456():
    from sys import *
    mod=10**9+7
    n,k=map(int,input().split())
    print(pow(2**k-1,n,mod))