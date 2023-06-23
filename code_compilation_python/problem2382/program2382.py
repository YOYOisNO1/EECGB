def program2382():
    x, y = map(int,input().strip().split())
    
    if x<0 and y<0:
    	print(x+y,0,0,x+y) 
    elif x<0 and y>0:
    	print(x-y,0,0,y-x)
    elif x>0 and y<0:
    	print(0,y-x,x-y,0)
    elif x>0 andy>0:  
    	print(0,x+y,x+y,0)