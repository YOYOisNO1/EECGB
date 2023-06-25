def program2502():
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    if(c==0):
    	if(a==b):
    		print("YES")
    	else:
    		print("NO")
    else:
    	if(c>0):
    		if(b<a):
    			print("NO")
    		else:
    			if((b-a)%c==0):
    				print("YES")
    			else:
    				print("NO")
    			
    	else:
    		if(b>a):
    			print("NO")
    		else:
    			if((a-b)%abs(c)==0):
    				print("YES")
    			else:
    				print("NO")