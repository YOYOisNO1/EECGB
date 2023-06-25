def program2335():
    n, m = map(int, input().split())
    a = ["." * (m + 2)]
    for i in range(0, n):
    	a.append("." + input() + ".")
    a.append("." * (m + 2))
    d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    ans = 0
    for i in range(1, n + 1):
    	for j in range(1, m + 1):
    		if a[i][j] == 'W':
    			for (dx, dy) in d:
    				if a[i + dx][j + dy] == 'P':
    					ans += 1
    					break
    print(ans)