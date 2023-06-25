def program1712():
    #!/usr/bin/env python
    
    import sys
    
    line = sys.stdin.readline().strip()
    groups = map(lambda x: int(x), line.split(" "))
    n = groups[0]
    m = groups[1]
    
    #n, m = 2, 4
    
    if (min(n, m) == 1):
        print(max(n,) m)
    
    elif (n > 2) and (m > 2):
        print((n) * m + 1) / 2
    
    else:
        c = n + m - 2
        x = c / 2
        y = c - x
        print((x) + 1) / 2 * 2 + (y + 1) / 2 * 2
    
       