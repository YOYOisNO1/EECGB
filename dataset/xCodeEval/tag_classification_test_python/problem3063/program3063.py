def program3063():
    from math import *
    
    
    l = list(map(int, input().split()))
    p = [(0, 0)]
    angle = 0
    for i in range(5):
    	p.append((p[-1][0] + l[i] * sin(angle), p[-1][1] + l[i] * cos(angle)))
    	angle += pi / 3
    ans = 0
    for i in range(1, 5):
    	ans += 0.5 * abs(p[i][0] * p[i+1][1] - p[i][1] * p[i+1][0])
    print(round(ans * 4 / sqrt(3)))