def program7651():
    from sys import stdin, stdout
    from decimal import Decimal
    
    n = int(stdin.readline())
    ans = 0
    
    l = 1
    label = 1
    x = (-1)
    EPS = 10 ** (-6)
    
    for i in range(n):
        
        x += (1.5)
        
        if label % 2:
            y = ((3) ** (0.5)) / (2)
        else:
            y = (3) ** (0.5)
        
        if x ** 2 + y ** 2 <= n ** 2 + EPS and (x + 0.5) ** 2 + (y - (3 ** 0.5) / 2) ** 2 <= n ** 2 + EPS:
            l, r = 1, n + 10
        else:
            label += 1
            break
        
        if label % 2:
            y = ((3) ** (0.5)) / (2)
        else:
            y = (3) ** (0.5)    
        
        while (r - l > 1):
            m = (r + l) // 2
            
            v1 = x ** 2 + ((m - 1) * (3 ** 0.5) + y) ** 2
            v2 = (x + 0.5) ** 2 + (((m - 1) * (3 ** 0.5) + y) - (3 ** 0.5) / 2) ** 2
            
            if x ** 2 + ((m - 1) * (3 ** 0.5) + y) ** 2 <= n ** 2 + EPS and (x + 0.5) ** 2 + (((m - 1) * (3 ** 0.5) + y) - (3 ** 0.5) / 2) ** 2 <= n ** 2 + EPS:
                l = m
            else:
                r = m
        
        if label % 2:
            if x == 0.5:
                ans += l * 2 - 1
            else:
                ans += (l * 2 - 1) * 2
        else:
            ans += 4 * l
            
        label += 1
        
    stdout.write(str(ans))