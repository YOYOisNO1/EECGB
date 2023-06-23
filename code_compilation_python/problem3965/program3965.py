def program3965():
    x1,y1,x2,y2 = map(int,input().split())
    
    ret = 0
    for y in range(y1,y2+1):
    	if y%2 == 0:
    		t = x1
    		if x1%2 == 1:
    			t += 1
    		for x in range(t,x2+1,2):
    			ret +=1
    	else:
    		t = x1
    		if x1%2 == 0:
    			t += 1
    		for x in range(t,x2+1,2):
    			ret += 1
    print(ret)