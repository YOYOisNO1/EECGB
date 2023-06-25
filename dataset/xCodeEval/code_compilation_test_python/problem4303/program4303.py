    from __future__ import division, print_function
    
def main():
        import __pypy__
        from collections import deque
    
        add = __pypy__.intop.int_add
        mul = __pypy__.intop.int_mul
    
        n, m, a, b = input_as_list()
        g, x, y, z = input_as_list()
    
    def next_(v):
            return add(mul(x, v), y) % z
    
    def sliding_minimum(a, k):
            dq = deque()
            out = []
            for i, e in enumerate(a):
                while dq and dq[-1] > e:
                    dq.pop()
                dq.append(e)
    
                if i >= k:
                    if dq[0] == a[i - k]:
                        dq.popleft()
    
                if i >= k - 1:
                    out.append(dq[0])
            return out
    
    
        prev = None
        tb = []
        for i in range(n):
            cur = []
            if prev is None:
                cur.append(g)
            else:
                cur.append(next_(prev))
    
            for _ in range(1, m):
                cur.append(next_(cur[-1]))
            prev = cur[-1]
            tb.append(cur)
    
        min_row = [sliding_minimum(tb[i], b) for i in range(n)]
    
        out = 0
        for c in range(len(min_row[0])):
            out += sum(sliding_minimum([min_row[i][c] for i in range(n)], a))
    
        print(out)
    
    INF = float('inf')
    MOD = 10**9 + 7
    
    import os, sys
    from atexit import register
    from io import BytesIO
    import itertools
    
    if sys.version_info[0] < 3:
        input = input
        range = xrange
    
        filter = itertools.ifilter
        map = itertools.imap
        zip = itertools.izip
    
    if "LOCAL_" in os.environ:
        debug_print = print
    else:
        sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
        sys.stdout = BytesIO()
        register(lambda: os.write(1, sys.stdout.getvalue()))
    
        input = lambda: sys.stdin.readline().rstrip('\r\n')
        debug_print = lambda *x, **y: None
    
    
def input_as_list():
        return list(map(int, input().split()))
    
def array_of(f, *dim):
        return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    
    main()