def program417():
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    leds = [int(x) for x in input().split()]
    ans = [-1 for x in range(n)]
    vals = [False for x in range(n)]
    
    ok = True
    for led,nxt in zip(leds,leds[1:]):
        val = ((nxt - led) % n)
        if val == 0:
            val = n
        old = ans[led - 1]
        if old == -1:
            if vals[val - 1]:
                ok = False
                break
            ans[led - 1] = val
            vals[val - 1] = True
        elif old != val:
            ok = False
            break
    else:
        rest = [x for x in range(1,n+1) if not vals[x - 1]]
        keys = [x for x in range(1,n+1) if ans[x - 1] == -1]
        for k,r in zip(keys,rest):
            ans[k - 1] = r
    
    if not ok:
        print(-1)
    else:
        for k,v in enumerate(ans):
            print(v,end=' ')
        print('')
    