def program2579():
    n = int(input())
    
    task = input()
    l = [[0,0]]
    drp = {}
    
    drp[(0,0)] = 1
    c = 0 
    
    for i in task :
    	if i == 'U' :
    		l.append([ l[-1][0] , l[-1][1]+1 ])
    		if tuple(l[-1]) not in drp :
    			drp[tuple(l[-1])] = 1
    		else:
    			drp[tuple(l[-1])] += 1
    	elif i == 'D' :
    		l.append([ l[-1][0] , l[-1][1]-1 ])
    		if tuple(l[-1]) not in drp :
    			drp[tuple(l[-1])] = 1
    		else:
    			drp[tuple(l[-1])] += 1
    	elif i == 'L' :
    		l.append([ l[-1][0]-1 , l[-1][1] ])
    		if tuple(l[-1]) not in drp :
    			drp[tuple(l[-1])] = 1
    		else:
    			drp[tuple(l[-1])] += 1
    	 else :
    		l.append([ l[-1][0]+1 , l[-1][1] ])
    		if tuple(l[-1]) not in drp :
    			drp[tuple(l[-1])] = 1
    		else:
    			drp[tuple(l[-1])] += 1
    for k,v in drp.items() :
    	if v >=2 :
    		c += (v*(v-1))//2
    
    print(c)