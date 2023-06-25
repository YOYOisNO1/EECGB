def program4517():
    import sys
    
    pin = sys.stdin.readline
    pout = sys.stdout.write
    
    
    ran=range
    t=int(pin())
    total=list(map(int,pin().split()))
    count=0
    maxe=max(total)+1
    while min(total)!=maxe:
    	mine=min(total)
    	count=count+1
    	for i in ran(t):
    		if total[i]%mine==0:
    			total[i]=maxe
    print(count)		