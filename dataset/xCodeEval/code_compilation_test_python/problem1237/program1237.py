def program1237():
    
    import math 
    a,b,s=map(int,input().split())
    while a,b,s!=0:
    	x=abs(a)+abs(b)
    	if x==s and s != 1:
    		print("YES")
    	elif x==s and s == 1:
    		print ("NO")
    	elif x>s:
    		print("NO")
    	elif s-x==1:
    		print("NO")
    	else: print ("YES")
    return 0
    
    	