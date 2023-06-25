def program472():
    #mudando para reenvio
    
    n = int(input())
    
    apples = [int(x) for x in input().split()]
    ap1 = 0
    ap2 = 0
    
    for i in apples:
    	if i==100:
    		ap1+=1
    	else:
    		ap2+=1
    if ap1>ap2:
    	if ap2==0:
    		if ap1%2==0:
    			print("YES")
    		else:
    			print("NO")
    	elif ap1%2==0:
    		print("YES")
    	else:
    		print("NO")
    elif ap1<ap2:
    	if ap1==0:
    		if ap2%2==0:
    			print("YES")
    		else:
    			print("NO")
    		
    	elif ap2%2==0:
    		if ap1%2==0:
    			print("YES")
    		else:
    			print("NO")
    	else:
    		if ap1%2==0:
    			print("YES")
    		else:
    			print("NO")
    else:
    	if ap1%2==0:
    		print("YES")
    	else:
    		print("NO")