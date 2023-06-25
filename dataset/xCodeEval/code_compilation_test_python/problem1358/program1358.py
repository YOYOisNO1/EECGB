def program1358():
    import sys
    from collections import deque
    
    n = int(sys.stdin.readline())
    q = deque()
    q.append((0, -1, 0))
    h = {}
    h[0] = {}
    h[0][0] = 1
    while q:
        # print q
        i, j, f = q.popleft()
        if i > n or 2 + 3 * (j+1) > n:
            continue
        jj = j + 1
        ii = i + 2 + 3*jj
        if ii not in h:
            h[ii] = {}
        if f + 1 not in h[ii]:
            h[ii][f+1] = 1
        q.append((ii, jj, f + 1))
        q.append((i, jj, f))
    
    if n in h:
        print len(h[n].values())
    else:
        print 0
    
    # for i, j in h.items():
    #     if i <= n:
    #         print i, j