    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    import sys, math, random, operator
    
    MOD = 10**9 + 7
    INF = 10**9
    
    pr = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")
    epr = lambda *args: sys.stderr.write(" ".join(str(x) for x in args) + "\n")
    die = lambda *args: pr(*args) ^ exit(0)
    
    read_str = input
    read_int = lambda: int(input())
    
    "---------------------------------------------------------------"
    
    n = read_int()
    s = read_str()
    
    num = []
    for i in xrange(len(s)):
        num.append([None])
        for j in xrange(i + 1, len(s)+1):
            num[i].append( int(s[i:j], 2) )
    
    needed_for_m = [None]
    cur = 0
    for x in xrange(1, 1000):
        cur += len(str(bin(x)[2:]))
        needed_for_m.append(cur)
    
    bins = [bin(x)[2:] for x in xrange(0, 1000)]
    
    cache = {}
def solve(state, used, maxm, pos):
        key = state, pos
        if key not in cache:
            res = 0
    
            # already good?
            # print("(%s)") % bin(state)[2:-1], maxm
            if state == (1 << (maxm + 1)) - 1:
                # print("good")
                res += 1
    
            # continue cuts
            for add in xrange(1, 100):
                if pos + add > len(s):
                    break
                val = num[pos][add]
                if val == 0:
                    continue
                if val >= 100:
                    break
    
                used2 = used
                if state & (1 << val) == 0:
                    used2 += len(bins[val] if val <= 100 else bin(val)[2:])
                maxm2 = max(maxm, val)
                pos2 = pos + add
                # print("pos"), pos, "+", add
                needed = needed_for_m[maxm2] if maxm2 <= 100 else INF
                if needed - used2 <= len(s) - pos2:
                    res += solve(state | (1 << val), used2, maxm2, pos2)
            cache[key] = res
        return cache[key]
    
    ans = 0
    for i in xrange(len(s)):
        cur = solve(1, 0, 1, i)
        ans += cur
        ans %= MOD
        epr(i, cur, ans)
    print(ans)