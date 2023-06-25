    # your code goes here
def free_way(p,i,j,dir):
    	if(dir == -1):
    		if(i==0):
    			return True
    		i-=1
    		while(i>= 0):
    			if(not (p[i][j] is ".") ):
    				return False
    			i-=1
    		return True
    	if(dir == 1):
    		if(i==7):
    			return True
    		i+=1
    		while(i<= 7):
    			if(p[i][j] != '.' ):
    				return False
    			i+=1
    		return True
    
    p=[]
    r=0
    while(r<8):
    	r+=1
    	tmp=input()
    	p.append( tmp )
    #print(p)
    move_a,move_b=10,10
    i=-1
    while(i<7):
    	i+=1
    	j=-1
    	while(j<7):
    		j+=1
    		if( (p[i][j]=='W')and ( free_way(p,i,j,-1) ) ):
    			move_a=i
    			break
    			#print("A:",i,j)
    	if(move_a !=10 ):
    		break
    i=8
    while(i>0):
    	i-=1
    	j=-1
    	while(j<7):
    		j+=1
    		if( (p[i][j]=='B')and ( free_way(p,i,j,1) ) ):
    			move_b=7-i
    			break
    			#print("B:",i,j)
    	if(move_b !=10 ):
    		break
    if(move_a <=move_b):
    	print("A")
    else:
    	print("B")
    