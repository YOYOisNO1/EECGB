def program153():
    M=10**9+7
    n,k=map(int,input().split())
    print(((n-k)**(n-k))%M*((k)**(k-1))%M)