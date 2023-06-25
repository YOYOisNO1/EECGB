    
    
def check_all(mat):
    
    	#top-left
    	if j+2<M and i+2<N:
    		if (mat[i][j+1] in (1,-1) and mat[i][j+2] in (1,-1) 
    			and mat[i+1][j] in (1,-1) and mat[i+1][j+2] in (1,-1)
    			and mat[i+2][j] in (1,-1) and mat[i+2][j+1] in (1,-1) and mat[i+2][j+2] in (1,-1)):
    
    			#convert all pos to -1's
    
    			mat[i][j+1] = -1
    			mat[i+1][j] = -1
    			mat[i+1][j+2] = -1
    			mat[i+2][j] = -1
    			mat[i+2][j+1] = -1
    			mat[i+2][j+2] = -1
    			return 1
    
    	#top
    	if j-1>=0 and j+1<M and i+2<N:
    		if all([ mat[i][j-1], mat[i][j+1], mat[i+1][j-1], mat[i+1][j+1], mat[i+2][j-1], mat[i+2][j], mat[i+2][j+1] ]):
    			mat[i][j-1] =  mat[i][j+1] =  mat[i+1][j-1] =  mat[i+1][j+1] =  mat[i+2][j-1] =  mat[i+2][j] =  mat[i+2][j+1] = -1
    			return 1
    
    
    	# top - right
    	if j-2>=0 and i+2<N:
    		if all([ mat[i][j-2], mat[i][j-1], mat[i+1][j-2], mat[i+1][j], mat[i+2][j-2], mat[i+2][j-1], mat[i+2][j] ]):
    			mat[i][j-2]= mat[i][j-1]= mat[i+1][j-2]= mat[i+1][j]= mat[i+2][j-2] = mat[i+2][j-1] = mat[i+2][j] = -1
    			return 1
    
    	#left
    	if i-1>=0 and i+1<N and j+2<M:
    		if all([ mat[i-1][j], mat[i-1][j+1], mat[i-1][j+2], mat[i][j+2], mat[i+1][j], mat[i+1][j+1], mat[i+1][j+2] ]):
    			mat[i-1][j]= mat[i-1][j+1]= mat[i-1][j+2]= mat[i][j+2]= mat[i+1][j]= mat[i+1][j+1]= mat[i+1][j+2] = -1
    			return 1
    
    	#right
    	if i-1>=0 and i+1<N and j-2>=0:
    		if all([ mat[i-1][j-2], mat[i-1][j-1], mat[i-1][j], mat[i][j-2], mat[i+1][j-2], mat[i+1][j-1], mat[i+1][j] ]):
    			mat[i-1][j-2]= mat[i-1][j-1]= mat[i-1][j]= mat[i][j-2]= mat[i+1][j-2]= mat[i+1][j-1]= mat[i+1][j] = -1
    			return 1
    
    	#bottom-left
    	if i-2>=0 and j+2<M:
    		if all( [mat[i-2][j], mat[i-2][j+1], mat[i-2][j+2], mat[i-1][j], mat[i-1][j+2], mat[i][j+1], mat[i][j+2] ]):
    			mat[i-2][j]= mat[i-2][j+1]= mat[i-2][j+2]= mat[i-1][j]= mat[i-1][j+2]= mat[i][j+1]= mat[i][j+2] = -1
    			return 1
    
    	#bottom
    	if i-2>=0 and j-1>=0 and j+1<M:
    		if all([mat[i-2][j-1], mat[i-2][j], mat[i-2][j+1], mat[i-1][j-1], mat[i-1][j+1], mat[i][j-1], mat[i][j+1]]):
    			mat[i-2][j-1]= mat[i-2][j]= mat[i-2][j+1]= mat[i-1][j-1]= mat[i-1][j+1]= mat[i][j-1]= mat[i][j+1] = -1
    			return 1
    
    	#bottom-right
    	if i-2>=0 and j-2>=0:
    		if all([mat[i-2][j-2], mat[i-2][j-1], mat[i-2][j], mat[i-1][j-2], mat[i-1][j], mat[i][j-2], mat[i][j-1] ]):
    			mat[i-2][j-2]= mat[i-2][j-1]= mat[i-2][j]= mat[i-1][j-2]= mat[i-1][j]= mat[i][j-2]= mat[i][j-1] = -1
    			return 1
    
    	return 0
    
    N, M = [int(x) for x in input().split()]
    
    mat = []
    for i in range(N):
    	temp = [1 if x=='#' else 0 for x in input()]
    	mat.append(temp)
    
    for i in range(N):
    	flag = 1
    	for j in range(M):
    
    		if mat[i][j]==1:
    
    			flag = check_all(mat)
    			if not flag:
    				break
    
    	if not flag:
    		break
    
    if not flag:
    	print("NO")
    else:
    	print("YES")