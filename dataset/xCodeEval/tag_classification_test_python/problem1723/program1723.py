def program1723():
    x, y, m = map(int, input().split())
    if x > y: x, y = y, x
    if y >= m: print(0)
    else:
    	if y <= 0: print(-1)
    	else:
    		cnt = 0
    		if x < 0:
    			cnt = abs(x) / y + 1
    			x += cnt * y
    		while max(x, y) < m:
    			x, y = x + y, max(x, y)
    			cnt += 1
    		print(cnt)
    