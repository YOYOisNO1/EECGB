def program3969():
    n,k=map(int,input().split())
    print ((k**k-1)*((n-k)**(n-k)))%(10**9+7)