def dp(curr, least, k, total, loc=0):
    	global d
    	if curr == total: return int(least == 0)
    	if d[curr][int(least==0)] != -1: return d[curr][int(least==0)]
    	for i in range(1, k+1):
    		if curr+i > total: break
    		loc+= dp(curr+i, 0 if least <= i else least, k, total)
    	d[curr][int(least==0)] = loc % 1000000007
    	return loc % 1000000007
    
    n, k, dd = map(int, input().split())
    d = [[-1, -1] for i in range(n)]
    print(dp(0, dd, k, n))