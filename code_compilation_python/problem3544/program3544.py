    import sys
    
def val(c):
        if c >= '0' and c <= '9':
            return ord(c) - ord('0')
        return ord(c) - ord('A') + 10
    
def ok(s, base, limit):
        sum = 0
        cur = 1
        t = s[::-1]
        for c in t:
            v = val(c)
            if v >= base:
                return False
            sum = sum + cur * v
            cur = cur * base
        return sum < limit
    
    t = sys.stdin.readline()
    t = t.rstrip()
    ind = t.find(':')
    h = t[0:ind]
    m = t[ind+1:]
    
    #print h,m
    
    if ok(h, 100, 24) and ok(m, 100, 60):
        print -1
        exit()
    
    ans = []
    base = 2
    while base <= 36:
        if ok(h, base, 24) and ok(m, base, 60):
            ans.append(base)
        base = base + 1
    if len(ans) == 0:
        print 0
        exit()
    print ans.pop(0),
    for val in ans:
        print val,
    print