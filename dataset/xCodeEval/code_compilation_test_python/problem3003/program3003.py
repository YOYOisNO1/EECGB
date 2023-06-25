    '''input
    3 6
    2H 3H 4H 5H 2S 3S
    6H 7H 8H 9H 4S 5S
    TH JH QH KH 6S 7S
    '''
    from sys import stdin
    import math
    from copy import deepcopy
    
def find_jokers(grid, n, m):
    	jokers = []
    	for i in range(n):
    		for j in range(m):
    			if grid[i][j] == 'J1' and len(jokers) > 0:
    				jokers.insert(0, [i, j])
    
    			elif (grid[i][j] == 'J1' or grid[i][j] == 'J2'):
    				jokers.append([i, j])
    			
    	return jokers
    
    
def get_remain(grid, n, m):
    	total = set()
    	for typ in ['D', 'S', 'H', 'C']:
    		for rank in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
    			total.add(rank + typ)
    	grid_set = set()
    	for i in range(n):
    		for j in range(m):
    			grid_set.add(grid[i][j])
    
    	r = total.difference(grid_set)
    	r = list(r)
    	return r
    
    
def replace(cgrid, x, y, item):
    	cgrid[x][y] = item
    
    
def first_condition(grid, x, y):
    	suit = set()
    	for i in range(x, x + 3):
    		for j in range(y, y + 3):
    			suit.add(grid[i][j][1])
    	if len(suit) == 1:
    		return True
    	else:
    		return False
    
    
def second_condition(grid, x, y):
    	rank = set()
    	for i in range(x, x + 3):
    		for j in range(y, y + 3):
    			rank.add(grid[i][j][0])
    	if len(rank) == 9:
    		return True
    	else:
    		return False
    
def check_mark(mark, x, y):
    	for i in range(x, x + 3):
    		for j in range(y, y + 3):
    			if mark[i][j] == True:
    				return False
    	else:
    		return True
    
    
def make_mark(mark, x, y):
    	for i in range(x, x + 3):
    		for j in range(y, y + 3):
    			mark[i][j] = True
    
    			
def check(grid, n, m):
    	count = 0
    	mark = [[False for x in range(m)] for y in range(n)]
    
    	for i in range(n):
    		if i + 3 <= n:
    			for j in range(m):
    				if j + 3 <= m:
    					if check_mark(mark, i, j):
    						if first_condition(grid, i, j) or second_condition(grid, i, j):
    								count += 1
    								make_mark(mark, i, j)
    								#print(mark)
    
    	if count >= 2:
    		return True
    	else:
    		return False
    
    
def get_ans(grid, n, m):
    	ans = []
    	mark = [[False for x in range(m)] for y in range(n)]
    
    	for i in range(n):
    		if i + 3 <= n:
    			for j in range(m):
    				if j + 3 <= m:
    					if check_mark(mark, i, j):
    						if first_condition(grid, i, j) or second_condition(grid, i, j):
    								ans.append([i, j])
    								make_mark(mark, i, j)
    								
    	return ans
    
    
    # main starts
    n, m = list(map(int, stdin.readline().split()))
    grid = []
    for _ in range(n):
    	grid.append(list(stdin.readline().split()))
    
    jokers = find_jokers(grid, n, m)
    remaining = get_remain(grid, n, m)
    #print(remaining)
    if len(jokers) == 2:
    	for i in range(len(remaining) - 1):
    		for j in range(i + 1, len(remaining)):
    			cgrid = deepcopy(grid)
    			fx, fy = jokers[0]
    			sx, sy = jokers[1]
    			replace(cgrid, fx, fy, remaining[i])
    			replace(cgrid, sx, sy, remaining[j])
    			if check(cgrid, n, m):
    				print('Solution exists.')
    				print('Replace J1 with ' + str(remaining[i])+ ' and J2 with '+ str(remaining[j])+ '.')
    				ans = get_ans(cgrid, n, m)
    				print('Put the first square to ' + '(' + str(ans[0][0] + 1) + ', ' + str(ans[0][1] + 1) + ').')
    				print('Put the second square to ' + '(' + str(ans[1][0] + 1) + ', ' + str(ans[1][1] + 1) + ').')
    				exit()
    				
    			else:
    				cgrid = deepcopy(grid)
    				replace(cgrid, sx, sy, remaining[i])
    				replace(cgrid, fx, fy, remaining[j])
    				if check(cgrid, n, m, ):
    					print('Solution exists.')
    					print('Replace J1 with ' + str(remaining[j])+ ' and J2 with '+ str(remaining[i])+ '.')
    					ans = get_ans(cgrid, n, m)
    					print('Put the first square to ' + '(' + str(ans[0][0] + 1) + ', ' + str(ans[0][1] + 1) + ').')
    					print('Put the second square to ' + '(' + str(ans[1][0] + 1) + ', ' + str(ans[1][1] + 1) + ').')
    					exit()
    				else:
    					pass
    
    elif len(jokers) == 1:
    	for i in range(len(remaining)):
    		cgrid = deepcopy(grid)
    		fx, fy = jokers[0]
    		replace(cgrid, fx, fy, remaining[i])
    		if check(cgrid, n, m):
    			print('Solution exists.')
    			print('Replace '+ str(grid[fx][fy]) +' with ' +  str(remaining[i]) +'.')
    			ans = get_ans(cgrid, n, m)
    			print('Put the first square to ' + '(' + str(ans[0][0] + 1) + ', ' + str(ans[0][1] + 1) + ').')
    			print('Put the second square to ' + '(' + str(ans[1][0] + 1) + ', ' + str(ans[1][1] + 1) + ').')
    			exit()
    				
    		else:
    			continue
    else:
    	if check(grid, n, m):
    		print('Solution exists.')
    		print("There are no jokers.")
    		ans = get_ans(grid, n, m)
    			
    		print('Put the first square to ' + '(' + str(ans[0][0] + 1) + ', ' + str(ans[0][1] + 1) + ').')
    		print('Put the second square to ' + '(' + str(ans[1][0] + 1) + ', ' + str(ans[1][1] + 1) + ').')
    		exit()
    	else:
    		pass
    
    print("No solution.")