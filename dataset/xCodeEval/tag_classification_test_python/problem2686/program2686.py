def program2686():
    w, h, k = map(int, input().split(" "))
    
    t = 0
    
    for i in range(k):
        t += (w * h) - (w - 2) * (h - 2)
        w -= 4
        h -= 4
    
    print(t)