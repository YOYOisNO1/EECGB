def program6566():
    #!/usr/bin/env python
    from collections import defaultdict
    n, k = map(int, input().split())
    a = map(int, input().split())
    
    
    m = 0
    for I in range(k):
        d = defaultdict(int)
        can = 0
        for i in range(I, n, k):
            d[a[i]] += 1
            can += 1
        if can == d[1] or can == d[2]:
            continue
        m += min(d.values())
    print(m)