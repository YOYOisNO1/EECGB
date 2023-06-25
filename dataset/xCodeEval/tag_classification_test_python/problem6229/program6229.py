    I = lambda : map(int, input().split())
    
def isrotation(a, b):
        for i in xrange(len(a)):
            if a[i:] + a[:i] == b: return a
    
    n, l = I()
    a = I()
    b = I()
    ans = None
    if n == 1:
        ans = "YES"
    else:
        ta = [0 for i in xrange(n)]
        tb = [0 for i in xrange(n)]
        ta[0] = l - a[-1] + a[0]
        tb[0] = l - b[-1] + b[0]
        for i in xrange(1,n):
            ta[i] = a[i] - a[i-1]
            tb[i] = b[i] - b[i-1]
        # print('ta:'),ta, 'tb', tb
        if isrotation(ta, tb):
            ans = "YES"
        else:
            ans = "NO"
    print(ans)