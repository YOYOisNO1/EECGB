def program498():
    n,k = map(int, input().split())
    l = [*map(int, input().split())]
    tot=sum(l)
    print(max([tot - sum(l[u::k])) for u in range(k)]))