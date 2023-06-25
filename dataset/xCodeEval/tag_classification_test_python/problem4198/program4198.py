def program4198():
    n = int(input())
    l = []
    for i in range(4*n+1):
    	x,y = map(int,input().split())
    	l.append([x,y])
    
    lx = sorted(l)
    ly = sorted(l,key = lambda x: x[1]) 
    
    x0 = lx[0][0]
    y0 = l[0][1]
    x1 = l[-1][0]
    y1 = l[-1][1]
    
    if x0 == lx[1][0]:
    	pass
    else:
    	x0 = lx[1][0]
    
    if y0 == ly[1][1]:
    	pass
    else:
    	y0 = ly[1][1]
    
    if x1 == lx[-2][0]:
    	pass
    else:
    	x1 = lx[-2][0]
    
    if y1 == ly[-2][1]:
    	pass
    else:
    	y1 = ly[-2][1]	
    
    for i in range(len(l)):
    	if (y0 == l[i][1] and x0 <= l[i][0] <= x1) or (x0 == l[i][0] and y0 <= l[i][1] <= y1) or (y1 == l[i][1] and x0 <= l[i][0] <=x1 ) or (x1 == l[i][0] and y0 <= l[i][1] <= y1):
    		pass
    	else:
    		print(l[i][0],l[i][1])