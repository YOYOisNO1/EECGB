def program1160():
    
    
    q, num = map(int, input().split())
    a, b = [], []
    
    
    for _ in range(q):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    
    
    min_time, max_time = sum(a), sum(b)
    
    if num < min_time or num > max_time:
        print("NO")
    else:
        print("YES")
        l = b.copy()
        tot = max_time
        i = len(b) - 1
        x = b[i]
        diff = max_time - num
    
    
        while diff != 0:
            if x == a[i]:
                i -= 1
                x = b[i]
            else:
                diff -= 1
                x -= 1
                l[i] -= 1
    
        print(*l)