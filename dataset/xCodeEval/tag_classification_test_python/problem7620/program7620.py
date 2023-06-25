def program7620():
    import sys
    inf=1000000000
    n=input()
    a=[map(int, input().split()) for i in range(n)]
    move=[None]*3
    move[0]=[[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
    move[1]=[[i, i] for i in range(-n+1, n)]+[[i, -i] for i in range(-n+1, n)]
    move[2]=[[i, 0] for i in range(-n+1, n)]+[[0, i] for i in range(-n+1, n)]
    dis=[[[[[[[inf, 0] for to_piece in range(3)] for from_piece in range(3)] for to_y in range(n) ] for to_x in range(n)] for from_y in range(n)] for from_x in range(n)]
    for from_x in range(n):
    	for from_y in range(n):
    		for from_piece in range(3):
    			q=[[from_x, from_y, from_piece]]
    			first=0
    			dis[from_x][from_y][from_x][from_y][from_piece][from_piece]=[0, 0]
    			while first<len(q):
    				cur_x, cur_y, cur_piece=q[first]
    				first+=1
    				cur_dis, cur_cnt=dis[from_x][from_y][cur_x][cur_y][from_piece][cur_piece]
    				for move_x, move_y in move[cur_piece]:
    					next_x, next_y=cur_x+move_x, cur_y+move_y
    					if 0<=next_x<n and 0<=next_y<n and dis[from_x][from_y][next_x][next_y][from_piece][cur_piece]>[cur_dis+1, cur_cnt]:
    						if dis[from_x][from_y][next_x][next_y][from_piece][cur_piece][0]==inf:
    							q.append([next_x, next_y, cur_piece])
    						dis[from_x][from_y][next_x][next_y][from_piece][cur_piece]=[cur_dis+1, cur_cnt]
    				for to_piece in range(3):
    					if dis[from_x][from_y][cur_x][cur_y][from_piece][to_piece]>[cur_dis+1, cur_cnt+1]:
    						if dis[from_x][from_y][cur_x][cur_y][from_piece][to_piece][0]==inf:
    							q.append([cur_x, cur_y, to_piece])
    						dis[from_x][from_y][cur_x][cur_y][from_piece][to_piece]=[cur_dis+1, cur_cnt+1]
    pos=[None]*(n*n+1)
    for x in range(n):
    	for y in range(n):
    		pos[a[x][y]]=[x, y]
    dp=[[[[inf, 0] for piece in range(3)] for y in range(n)] for x in range(n)]
    dp[pos[n*n][0]][pos[n*n][1]]=[[0, 0], [0, 0], [0, 0]]
    for value in range(n*n-1, 0, -1):
    	cur_x, cur_y=pos[value]
    	next_x, next_y=pos[value+1]
    	for from_piece in range(3):
    		for to_piece in range(3):
    			a=dp[next_x][next_y][to_piece]
    			b=dis[cur_x][cur_y][next_x][next_y][from_piece][to_piece]
    			dp[cur_x][cur_y][from_piece]=min(dp[cur_x][cur_y][from_piece], [a[0]+b[0], a[1]+b[1]])
    result=dp[pos[1][0]][pos[1][1]]
    result=min(result[0], result[1], result[2])
    print(result[0],) result[1]