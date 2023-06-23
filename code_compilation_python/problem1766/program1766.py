def program1766():
    from sys import stdin
    n,k,x = map(int,stdin.readline().split())
    a = map(int,stdin.readline().split())
    print sum(a[:k])+k*x