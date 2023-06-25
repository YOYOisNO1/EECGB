def program288():
    t, s, x = map(int, input().split())
    
    if x < t + s:
        print("YES") if x - t == 0 else "NO"
    else:
        print("YES") if (x - t) % s == 0 or (x - t) % s - 1 == 0 else "NO"