def program1647():
    a,b = input().split()
    tot = a[0]
    
    for i in range(1, len(a)):
    	if(a[i] < b[0]):
    		tot+=a[i]
    	else:
    		tot+=b[0]
    		break
    if(a == tot)
    	tot+= b[0]
    
    print(tot)