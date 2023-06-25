def get_toupdate(p):
    	return [(p + 1) % 8, (p + 7) % 8]
    res = [[0 for x in xrange(500)] for y in xrange(500)]
    x = 199
    y = 200
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    update = [[x, y, 1]]
    update2 = []
    n = int(input())
    data = map(int, input().split())
    for i in data:
    	mp = {}
    	for j in update:
    		tx = j[0]
    		ty = j[1]
    		for k in range(i):
    			tx += dx[j[2]]
    			ty += dy[j[2]]
    			res[tx][ty] = 1
    		toupdate = get_toupdate(j[2])
    		for nxt in toupdate:
    			if (tx, ty, nxt) not in mp:
    				update2.append([tx, ty, nxt])
    				mp[(tx, ty, nxt)] = 1
    	update = []
    	for j in update2:
    		update.append(j)
    	update2 = []
    cnt = 0
    for i in res:
    	for j in i:
    		if j == 1:
    			cnt += 1
    print(cnt)