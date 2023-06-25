def program130():
    n,a,b = map(int, input().split())
    diff = abs(a-b)
    if a>b:
    	a ,b= b,a
    l = [i for i in range(1,n+1)]
    flag = True
    k=n
    rounds =1
    while flag:
    
    	k=len(l)
    	if k==2:
    		print("Final!")
    		flag = False
    		break
    	rm = []
    	tmp =[]
    	#print(l)
    	for i in range(0,k-1,2):
    		c = l[i]
    		d =l[i+1]
    		if c == a and b==d:
    			print(rounds)
    			flag =False
    		elif c == a:
    			tmp.append(c)
    		elif d == a:
    			tmp.append(d)
    		elif c == b:
    			tmp.append(c)
    		elif d == b:
    			tmp.append(d)
    		else:
    			tmp.append(c)
    	l = tmp[:]
    	rounds += 1
    
    	#print("hello")