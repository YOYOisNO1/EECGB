def nextc(m):
        m2 = {}
        for n, c in m.iteritems():
            h = n-1 >> 1
            m2[h] = m2.get(h, 0) + c
            m2[n-1 - h] = m2.get(n-1 - h, 0) + c
        return m2
    
def countseg(l, s, cache={}):
        if s > l: return 0
        if s == l: return 1
        if (l, s) in cache:
            return cache[l, s]
        h = l-1 >> 1
        out = countseg(h, s) + countseg(l-1 - h, s)
        cache[l, s] = out
        return out
        
def findx(l, q, ss):
        if l <= max(ss):
            return (l-1 >> 1) + q
        h = l-1 >> 1
        ns = sum(countseg(h, s) for s in ss)
        if q >= ns:
            return h + 1 + findx(l-1 - h, q - ns, ss)
        else:
            return findx(h, q, ss)
    
def f(l, r):
        m = {l: 1, l-1: 0}
        q = 1
        while r >= q and min(m) > 2:
            r -= q
            q <<= 1
            m = nextc(m)
        mn, mx = min(m), max(m)
        if mx & 1:
            if r >= m[mx]:
                if mx == 3:
                    return findx(l, r - m[mx], [1,2])
                return findx(l, r - m[mx], [mn])
            else:
                return findx(l, r, [mx])
        else:
            return findx(l, r, [mn, mx])
    
def ans(n, k):
        if k == 1: return 1
        if k == 2: return n
        return 2 + f(n - 2, k - 3)
        
def brute_ans(n, k):
        if k == 1: return 1
        if k == 2: return n
        return 2 + brute_f(n - 2, k - 2)
        
def brute_f(l, r):
        s = [(0, l)]
        for _ in xrange(r):
            i = max(xrange(len(s)), key=lambda j: s[j][1]-1 >> 1)
            x, d = s[i]
            h = d-1 >> 1
            s = s[:i] + [(x, h), (x+h+1, d-1-h)] + s[i+1:]
        return x+h
    
def test_n(n):
        for i in xrange(1, n + 1):
            assert brute_ans(n, i) == ans(n, i)
    
    if __name__ == '__main__':
        n, k = map(int, input().split())
        print ans(n, k)