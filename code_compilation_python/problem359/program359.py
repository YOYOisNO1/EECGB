def fact(n):
    	p = 1
    	if(n == 0): 
    		return 1
    	for i in range(1,n+1):
    		p = p*n
    	return p
    n = int(input())
    f = fact(n+1)
    a = map(int, input().split())
    a.pop(0)
    b = map(int, input().split())
    b.pop(0)
    for i in range(f):
    	if(a[0]>b[0]):
    		a.append(b[0])
    		a.append(a[0])
    		a.pop(0)
    		b.pop(0)
    	elif(b[0]>a[0]):
    		b.append(a[0])
    		b.append(b[0])
    		a.pop(0)
    		b.pop(0)
    	else:
    		print "-1"
    		exit()
    	if(len(a)==0):
    		print str(i+1)+" "+"2"
    		exit()
    	elif(len(b)==0):
    		print str(i+1)+" "+"1"
    		exit()
    print "-1"