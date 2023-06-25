def program3017():
    u, v = map(int, input().split())
    if u&1^v&1 or u > v:
        print(-1)
        exit()
    if not u and not v:
        print(0)
        exit()
    if u == v:
        print(1)
        print(u)
        exit()
    _and = (v - u)//2
    c = int(u + _and)
    d = int(_and)
    if c^d == u:
        print(2)
        print(c, d)
        exit()
    print(3)
    print((v - u)//2, u, (v - u)//2)