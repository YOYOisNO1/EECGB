def program3301():
    from sys import stdin, stdout
    from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial
    
    n = int(stdin.readline())
    mp = {}
    
    d = 2
    while d * d <= n:
        while n % d == 0:
            
            if d not in mp:
                mp[d] = 1
            else:
                mp[d] += 1
            
            n //= d
        
        d += 1
    
    if n != 1:
        mp[n] = 1
    
    ans = 1
    cnt = 1
    s = set()
    
    for v in mp:
        ans *= v
        cnt = max(cnt, mp[v])
        s.add(mp[v])
    
    
    for i in range(20):
        if (1 << i) == cnt and len(s) <= 1:
            stdout.write(str(ans) + ' ' + str(i) + '\n')
            break
        
        if (1 << i) >= cnt:
            stdout.write(str(ans) + ' ' + str(1 + i) + '\n')
            break