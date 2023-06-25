    s = list(map(int,input().split()))
    
    
def dis(a,b,c,d):
    	 return ((a-c)**2 + (b-d)**2)
    
def ass(s):
    	a,b,c,d,e,f = s
    	AB = dis(a,b,c,d)
    	BC = dis(c,d,e,f)
    	CA = dis(e,f,a,b)
    
    	x = max(AB,BC,CA)
    	
    	return x == AB+BC+CA-x and AB and BC and CA
    
    if ass(s):
    	print("RIGHT") 
    	exit()
    
    for i in range(6):
    	s[i] -= 1
    	if ass(s): print("ALMOST");exit()
    	s[i] += 2
    	if ass(s): print("ALMOST");exit()
    	s[i] -=1
    
    print("NEITHER") 