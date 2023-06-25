def program1549():
    [p, k] = map(int, input().split())
    #g = [-1] * p
    #for i in range(p):
    #    parent = (i * k) % p
    #    g[i] = parent
    #comps = 0; vis = [False] * p
    #for i in range(1,p):
    #    if not vis[i]: comps += 1
    #    cur = i
    #    while cur > 0 and not vis[cur]:
    #        vis[cur] = True; cur = g[cur]
    if k == 0: print(pow(p,) p - 1, pow(10,9) + 7)
    elif k == 1: print(pow(p,) p, pow(10,9) + 7)
    else:
        ord_k = 1; k_pow_ord = k
        while k_pow_ord != 1:
            ord_k += 1
            k_pow_ord = (k * k_pow_ord) % p
        comps = (p - 1) / ord_k
        print(pow(p,) comps, pow(10,9) + 7)