def program5446():
    from copy import copy
    
    MAX_N = 100
    n, m = map(int, input().strip().split())
    a = [int(x) for x in input().strip().split()]
    d = [0 for x in range(MAX_N + 1)]
    
    tot = 0
    for x in a:
        d[x] += 1
        tot = max(d[x], tot)
    
    m = 0
    solved = False
    for x in range(tot, 0, -1):
        dd = copy(d)
        cnt = 0
        for i in range(1, MAX_N+1):
            while dd[i] >= x:
                dd[i] -= x
                cnt += 1
            if cnt >= n:
                print(x)
                solved = True
                break
        if solved:
            break
        
    if not solved:
        print(0)