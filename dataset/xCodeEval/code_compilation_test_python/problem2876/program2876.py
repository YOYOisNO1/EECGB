def program2876():
    from sys import stdin
    
    p = stdin.readline().strip()
    
    d = dict()
    
    for i in range(10):
        d[stdin.readline().strip()] = i
    
    ans = ''
    
    for i in range(9):
        ans += str(d[p[10*i:10*(i+1)]]))
    
    print(ans)