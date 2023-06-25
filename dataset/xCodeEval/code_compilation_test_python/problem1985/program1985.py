    sides = list(map(int,input().split()))
     
     
def leng(a,b,c,d):
    	 return ((a-c)**2 + (b-d)**2)
     
def ass(sides):
    	a,b,c,d,e,f = sides
    	AB = leng(a,b,c,d)
    	BC = leng(c,d,e,f)
    	CA = leng(e,f,a,b)
     
    	x = max(AB,BC,CA)
    	
    	return x == AB+BC+CA-x and AB and BC and CA
     
    if ass(sides):
    	print("RIGHT") 
    	exit()
     
    for i in range(6):
    	sides[i] -= 1
    	if ass(sides): print("ALMOST")
            exit()
    	sides[i] += 2
    	if ass(sides): print("ALMOST")
            exit()
    	sides[i] -=1
     
    print("NEITHER")