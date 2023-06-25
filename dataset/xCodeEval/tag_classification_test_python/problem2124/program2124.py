def ii():
        return map(int, input().split())
    n, k, d = ii()
def mod(x):
        return x % 1000000007
    if d > n:
        print(0)
        exit()
    w_d = [None]*(n+1)
    wo_d = [None]*(n+1)
    w_d[d] = 1
    for i in xrange(d):
        w_d[i] = 0
    wo_d[0] = 1
def calc(i, dp):
        global k, d, w_d, wo_d
        if dp:
            if wo_d[i] is None:
                ans = 0
                for j in xrange(1, k+1):
                    if j <= i:
                        ans += calc(i-j, True)
                    else:
                        break
                wo_d[i] = mod(ans)
            return wo_d[i]
        else:
            if w_d[i] is None:
                ans = 0
                for j in xrange(1, k+1):
                    if j <= i:
                        ans += calc(i-j, j >= d)
                    else:
                        break
                w_d[i] = mod(ans)
            return w_d[i]
    print(calc(n,) False)