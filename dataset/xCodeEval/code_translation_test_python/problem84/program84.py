    from collections import defaultdict, OrderedDict
    InputList = lambda Dtype : [Dtype(x) for x in input().split()]
def solve():
    	N = int(input())
    	ans = [0,3,5,7,8]
    	if N < 5: return ans[N]
	def valid(x):
    		return x % 4 == 0 or x & 1
	def loc(x):
    		p = x-1
    		done_upto = (p+1)//2 - 1 + (p//4) - 1
    		return done_upto+1 if valid(x) else done_upto
    	Min = 0; Max = 3*10**9
    	while Min < Max:
    		Mid = (Min+Max)//2
    		if loc(Mid) == N:
    			return Mid if valid(Mid) else Mid-1
    		if loc(Mid) < N:
    			Min = Mid+1
    		else:
    			Max = Mid
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
    
    ReturnMode = True
    t = 1
    
    if not t: t = int(input())
    
    if ReturnMode:
    	for _ in range(t):
    		ans = solve()
    		if type(ans) == list: print(*ans)
    		else: print(ans)
    else: 
    	for _ in range(t): solve()