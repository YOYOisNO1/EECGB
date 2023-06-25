def program1828():
    cantidad=input()
    sol=[]
    for i in range(cantidad):
    	pieza=input()
    	while(pieza>0):
    		if(pieza%3==0 or pieza%7==0):
    			sol.append("YES")
    			break
    		else:
    			pieza=pieza-3
    	if(pieza<0):
    		sol.append("NO")
    
    for j in range(len(sol)):
    	print(sol[j])