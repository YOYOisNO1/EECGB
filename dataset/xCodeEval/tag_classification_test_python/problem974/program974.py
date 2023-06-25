def program974():
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    mn = max(a[0]-(b[0]+b[2]), 0) + max(a[1]-(b[1]+b[0]), 0) + max(a[2]-(b[2]+b[1]),0)
    mx = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    
    print(mn, mx)