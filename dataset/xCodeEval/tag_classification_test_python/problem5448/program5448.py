def program5448():
    s = input()
    lst = s.split(' ')
    lst[0], lst[1], lst[2] = int(lst[0]), int(lst[1]), int(lst[2])
    g_max = 0
    path = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    for i in xrange(8):
    	itm = path[i]
    	a = lst[0] - itm[0] * 3
    	b = lst[1] - itm[1] * 3
    	c = lst[2] - itm[2] * 3
    	if a < 0 or b < 0 or c < 0:
    		continue
    	g_max = max(g_max, a // 3 + b // 3 + c // 3 + min(a % 3 + itm[0] * 3, b % 3 + itm[1] * 3 , c % 3 + itm[2] * 3))
    print(g_max)