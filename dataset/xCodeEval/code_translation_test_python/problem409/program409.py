def program409():
    p,x,y=map(int,input().split())
    i=0
    while x-y>=50:
    	x-=50
    	i-=1
    while True:
    	d=(x//50)%475
    	for temp in range(25):
    		d=(d*96+42)%475
    		if p==d+26:
    			i=int(round(i))
    			print(max((2*i+1)/2,0))
    			exit(0)
    	if i>=0:
    		i+=0.5
    		x+=50 
    	else:
    		i+=1
    		x+=50