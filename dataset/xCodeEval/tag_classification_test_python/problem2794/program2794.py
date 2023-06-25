def program2794():
    import sys
    import math
    
    w, h = (map(int, sys.stdin.readline().split()))
    w1, h1 = (map(int, sys.stdin.readline().split()))
    w2, h2 = (map(int, sys.stdin.readline().split()))
    
    for i in range(h, -1, -1):
        w+=i
        w = max(w, 0)
        if i == h1:
            w-=w1
        if i == h2:
            w-= w2
        w = max(w, 0)
    print(w)