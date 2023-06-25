def program507():
    import math
    import sys
    
    n = int(input())
    coords = []
    for i in range(n):
        coords.append(map(int, input().split()))
    
    sorted(coords, key = lambda x : x[0]) # sorted by x-value now 
    
    if len(coords) == 1:
        print(-1) 
    
    elif len(coords) == 2: 
        if coords[0][0] == coords[1][0]:
            print(-1)
        elif coords[0][1] == coords[1][1]:
            print(-1)
        else:
            print(abs((coords[1][1]) - coords[0][1]) * (coords[1][0] - coords[0][0]))
    
    elif len(coords) >= 3:
        maxx = max(coords[i][0] for i in range(len(coords)))
        minx = min(coords[i][0] for i in range(len(coords)))
        maxy = max(coords[i][1] for i in range(len(coords)))
        miny = min(coords[i][1] for i in range(len(coords)))
        print(abs((maxx) - minx) * (maxy - miny))
    