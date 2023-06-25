def program3415():
    c=map(lambda n: (n+1)/2, map(int, input().split()))
    n=max(c)
    print(3*n-c[::-1].index(n)+29)