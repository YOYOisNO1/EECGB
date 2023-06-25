def dist(p, q):
    	return abs(p[0] - q[0]) + abs(p[1] - q[1])
     
def go(i, tt):
    	global pts
    	ans = 0
    	for j in range(0, i + 1):
    		for k in range(i, 64):
    			jk = dist(pts[i], pts[j]) + dist(pts[j], pts[k])
    			kj = dist(pts[i], pts[k]) + dist(pts[k], pts[j])
    			if jk <= tt or kj <= tt:
    				ans = max(ans, abs(j - k) + 1)
    	return ans
     
    x0, y0, ax, ay, bx, by = map(int, input().split())
    xs, ys, t = map(int, input().split())
     
    pts = [[] for i in range(64)]
    pts[0] = [x0, y0]
    for i in range(1, 64):
            xi = ax * pts[i - 1][0] + bx
            yi = ay * pts[i - 1][1] + by
            pts[i] = [xi, yi]
     
    ans = 0
    s = [xs, ys]
    for i in range(64):
    	tt = t - dist(s, pts[i])
    	if tt >= 0:
    		ans = max(ans, go(i, tt))
    print(ans)
    