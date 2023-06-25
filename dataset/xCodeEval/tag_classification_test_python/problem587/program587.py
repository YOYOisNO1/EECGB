def program587():
    x, y, z = map(int, input().strip().split())
    x1, y1, z1 = map(int, input().strip().split())
    a = map(int, input().strip().split())
    
    ans = 0
    
    if y < 0: ans += a[0]
    elif y > y1: ans += a[1]
    
    if z < 0: ans += a[2]
    elif z > z1: ans += a[3]
    
    if x < 0: ans += a[4]
    elif x > x1: ans += a[5]
    
    print(ans)