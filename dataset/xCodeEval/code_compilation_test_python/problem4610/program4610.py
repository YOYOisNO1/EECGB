    from functools import cmp_to_key
    
def read_ints():
    	return tuple(map(int, input().split()))
    
    n, m, d = read_ints()
    a = [read_ints() for _ in range(n)]
    b = [read_ints() for _ in range(m)]
    
    @cmp_to_key
def cmp(x, y):
    	if x[0] != y[0]:
    		return  y[0] - x[0] 
    	return x[1] - y[1]
    
    a.sort(key=cmp)
    b.sort(key=cmp)
    
    
    j = -1
    val = b[0][0]
    cw = b[0][1]
    while j < n-1 and cw + a[j+1][1] <= d:
    	j += 1
    	cw += a[j][1]
    	val += a[j][0]
    
    sol = 0
    if j >= 0:
    	sol = val
    
    for i in range(1, m):
    	cw += b[i][1]
    	val += b[i][0]
    	while j > 0 and cw > d:
    		cw -= a[j][1]
    		val -= a[j][0]
    		j -= 1
    
    	if j > 0:
    		sol = max(sol, val)
    	else:
    		break
    
    print(sol)