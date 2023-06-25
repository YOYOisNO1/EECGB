    #!/usr/bin/python
    
def ia(): return map(int, input().split())
    
    n, k = ia()
    
    a = list(input())
    n = len(a)
    
    b = n * [None]
    e = n * [None]
    
def beg(b):
        s = set()
        for i, e in enumerate(a):
            if e in s: continue
            else     : b[i] = e; s.add(e)
    
def end(b):
        n = len(a)
        s = set()
        for i in xrange(n):
            j = n - i - 1
            if a[j] in s: continue
            else     : b[j] = a[j]; s.add(a[j])
    
    beg(b)
    end(e)
def solve():
        n = len(a)
        m = 0
        for i in xrange(n):
            if b[i] != None: m += 1
            if m > k: return "YES"
            if e[i] != None: m -= 1
        return "NO"
    
    
    print(solve())