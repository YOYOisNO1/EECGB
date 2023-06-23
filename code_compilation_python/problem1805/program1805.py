def program1805():
    s1 = input().strip()
    s2 = input().strip()
    n=len(s1)
    c=0
    i=0
    while i<n-1:
    	a = s1[i:i+2]
    	b = s2[i:i+2]
    	if(a=="00" and b=="0X"):
    		c+=1
    		i+=2
    	elif(a=="X0" and b=="00"):
    		c+=1
    		i+=2
    	elif(a=="0X" and b=="00"):
    		c+=1
    		i+=2
    	elif(a=="00" and b=="X0"):
    		c+=1
    		i+=2
    	elif(a=="00" and b=="00"):
    		c+=1
    		if i<n-2 and s1[i+2]=='0' and s2[i+2]=='0':
    			i+=1
    			c+=1
    		i+=2
    	else:
    		i+=1
    		
    print(c)