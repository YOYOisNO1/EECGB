def program2532():
    i = input() 
    l = i.split(' ')
    l.sort()
    if(len(set(l))==1) :
    	print(0)
    else :
    	num = [int(x[0],10) for x in l]
    	st = [x[1] for x in l]
    	if(len(set(st))==1) :
    		if(num[1]-num[0]==1 or num[2]-num[1]==1) :
    			if(num[1]-num[0]==1 and num[2]-num[1]==1) :
    				print(0)
    			else :
    				print(1)
    		else :
    			if(num[1]-num[0]==2 or num[2]-num[1]==2 or num[1]-num[0]==0 or num[2]-num[1]==0) :
    				print(1)
    			else :
    				print(2)
    	elif(len(set(st))==2) :
    		merge = [[st[i],num[i]] for i in range(len(st))]
    		merge.sort()
    		if(merge[0][0]==merge[1][0]) :
    			if(merge[0][1]-merge[1][1]==-1 or merge[0][1]-merge[1][1]==1 or merge[0][1]-merge[1][1]==-2 or merge[0][1]-merge[1][1]==2 or merge[0][1]-merge[1][1]==0 ) :
    				print(1)
    			else :
    				print(2)
    		elif(merge[1][0]==merge[2][0]) :
    			if(merge[1][1]-merge[2][1]==-1 or merge[1][1]-merge[2][1]==1 or merge[1][1]-merge[2][1]==-2 or merge[1][1]-merge[2][1]==2 or merge[1][1]-merge[2][1]==0 ) :
    				print(1)
    			else :
    				print(2)
    	else :
    		print(2)
    