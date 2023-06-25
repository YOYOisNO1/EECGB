    """
    	#TLE
    	# Multidimensional list initialization takes too much time
    	# Corresponding C++ code is accepted.
    	Author		: Arif Ahmad
    	Date  		: 
    	Algo  		: 
    	Difficulty	: 
    """
    
    
    t 		= []
    grid 	= [[False for i in range(302)] for j in range(302)]
    n 		= None
    dx		= [0, 1, 1, 1, 0, -1, -1, -1]
    dy 		= [1, 1, 0, -1, -1, -1, 0, 1]
    dp 		= [[[[False for i in range(8)] for j in range(31)] for k in range(302)] for m in range(302)]
    
def visit(i, x, y, dr):
    	if dp[x][y][i][dr]: return
    	dp[x][y][i][dr] = True
    
    	global grid
    	for k in range(t[i]):
    		x += dx[dr]
    		y += dy[dr]
    		grid[x][y] = True
    
    	if (i + 1) < n:
    		visit(i+1, x, y, (dr + 1) % 8)
    		visit(i+1, x, y, (dr + 7) % 8)
    	
    
def main():
    	global n, t
    	n = int(input())
    	t = [int(_) for _ in input().split()]
    
    	visit(0, 150, 149, 0)	
    	print(sum(x.count(1) for x in grid))
    
    
    if __name__ == '__main__':
        main()
        