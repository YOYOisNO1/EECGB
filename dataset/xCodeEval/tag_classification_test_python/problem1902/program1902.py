    # coding: utf
    
def sign(x): 
        return 1 if x >= 0 else -1
    	
    x,y = map(int, input().split())
    l = abs(x) + abs(y);
    if (x>0):
    	print(0,) l*sign(y), l, 0
    else:
    	print(-l,) 0, 0, l*sign(y)