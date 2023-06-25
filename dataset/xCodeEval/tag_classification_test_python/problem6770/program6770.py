    from sys import stdin
    from bisect import bisect_right as br
    
    INF = float('inf')
    
    n, m = map(int, input().strip().split())
    k = map(int, input().strip().split())
    
    tot = sum(k)
    
    inp = stdin.readlines()
    days = [[INF] for i in xrange(n)]
    offers = []
    
def cando(d):
        global n, tot, days, offers
        
        rem = tot   # upgrades remaining to be bought
        have = 0    # amount of money currently having
    
        last = [0 for i in xrange(n)]
        for t in xrange(n):
            last[t] = days[t][max(0, br(days[t], d) - 1)]
    
        temp = [k[i] for i in xrange(len(k))]
        
        for day in xrange(1, d + 1):
            have += 1
            
            try: typesonsale = offers[day]
            except: typesonsale = []
            for t in typesonsale:
                if temp[t] == 0: continue
                if day == last[t]:
                    buy = min(have, temp[t])
                    temp[t] -= buy
                    have -= buy
                    rem -= buy
    
        return 2 * rem <= have
    
    for line in inp:
        d, t = map(int, line.strip().split())
        t -= 1
        days[t].append(d)
        while d >= len(offers):
            offers.append([])
        offers[d].append(t)
    
    for i in xrange(n): days[i].sort()
    
    lo = 1
    hi = tot << 1
    
    while lo < hi:
        mid = (lo + hi) >> 1
    
        if cando(mid):
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)