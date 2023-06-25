def program3669():
    n = int(input())
    l = []
    for i in xrange(n):
    	a = float(input())
    	l.append(a)
    
    if n == 0:
    	print("YES")
    	print(1)
    	print(1)
    	print(3)
    	print(3)
    
    if n == 1:
    	print("YES")
    	print(int(l[0]))
    	print(int(l[0]*3))
    	print(int(l[0]*3))
    
    if n == 4:
    	k = sorted(l)
    	if k[3]-k[0] == (k[2]+k[1])/2 and k[3]-k[0] == sum(k)/4:
    		print("YES")
    	else:
    		print("NO")
    
    if n == 2:
    	a1, a2 = l[0], l[1]
    	if a1>a2:
    		a1, a2 = a2, a1
    	if int(4*a1-a2>=0) and int(3*a1)>=0:
    		print("YES")
    		print(int(4*a1-a2))
    		print(int(3*a1))
    	else:
    		print("NO")
    
    if n == 3:
    	m = sorted(l)
    	a1, a2, a3 = m[0], m[1], m[2]
    	a4 = a1 + (a2+a3)/2
    	if ((a4+a1+a2+a3)/4==a4-a1 and a4>=1 and a4<=1000000):
    		print("YES")
    		print(int(a4))
    	else:
    		a4=2*a3-2*a1-a2
    		if ((a4+a1+a2+a3)/4==a3-a1 and a4>=1 and a4<=1000000):
    			print("YES")
    			print(int(a4))
    		else:
    			 a4 = a3-(a1+a2)/2
    			 if ((a4+a1+a2+a3)/4==(a2+a1)/2 and a4>=1 and a4<=1000000):
    				 print("YES")
    				 print(int(a4))
    			 else:
    				print("NO")