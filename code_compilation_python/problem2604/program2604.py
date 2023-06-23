    n = int(input())
    days = list(map(int, input().split(' ')))
    
    min_rest = 1000
    
def dfs(day, prev_act, rest):
    	if day == n:
    		global min_rest
    		min_rest = min(min_rest, rest)
    		return
    	d = days[day]
    	if (d == 1 or d == 3) and prev_act != 0:
    		dfs(day + 1, 0, rest)
    	if (d == 2 or d == 3) and prev_act != 1:
    		dfs(day + 1, 1, rest)
    	dfs(day + 1, -1, rest + 1)
    			
    dfs(0, -1, 0)
    print(min_rest)