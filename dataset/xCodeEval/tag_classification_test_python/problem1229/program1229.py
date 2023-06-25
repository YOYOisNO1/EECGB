def program1229():
    q = int(input())
    l = list(map(int, input().split()))
    a = max(l)
    if l.count(a) > 1:
        print(a, a)
        exit(0)
    ll = [1]
    for i in range(q):
        if a % l[i] != 0 or l.count(l[i]) > 1:
            ll += [l[i]]
    print(a, max(ll))