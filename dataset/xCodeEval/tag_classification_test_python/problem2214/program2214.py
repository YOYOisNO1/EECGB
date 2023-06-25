    from functools import lru_cache 
    n,x = list(map(int,input().split()))
    @lru_cache(maxsize=None)
def dp(nn,xx):
    	y = str(xx)
    	if len(y)==nn:
    		return 0 
    	res = 1e9 
    	for j in y:
    		if int(j)>1:
    			res = min(res,1 + dp(nn,xx*int(j)))
    	return res 
    res = dp(n,x)
    if res>=1e9:
    	print(-1)
    else:
    	print(res)