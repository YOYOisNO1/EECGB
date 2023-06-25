def program7908():
    import sys
    n, m, k = map(int, sys.stdin.readline().split())
    data = []
    for i in xrange(n):
        tmp = sys.stdin.readline()
        items = []
        for j in xrange(m):
            item = map(int, sys.stdin.readline().split())
            items.append(item)
        data.append(items)
    ans = 0
    
    for i in xrange(n):
        for j in xrange(n):
            if i == j: continue
            ii = data[i]
            ij = data[j]
            cat = []
            for l in xrange(m):
                buyinfo = ii[l]
                sellinfo = ij[l]
                profit = sellinfo[1] - buyinfo[0]
                num = buyinfo[2]
                if profit > 0 and num > 0:
                    cat.append([profit, num])
            cat.sort(reverse=True)
            rem = k
            tmp = 0
            for (profit, num) in cat:
                n_ = min(num, rem)
                tmp += profit * n_
                rem -= n_
                if rem == 0:
                    break
            #print(i,) j, tmp
            ans = max(ans, tmp)
    print(ans)