def program591():
    a=[]
    a.append("4")
    a.append("7")
    p=[]
    p.append("4")
    p.append("7")
    j=0
    for i in range(1,200):
    	xx=[]
    	l=2*(i-1)
    	r=2*i
    	for j in range(l,r):
    		x=a[j]+"4"
    		a.append(x)
    		x=a[j]+"7"
    		a.append(x)
    b=[]
    for x in a:
    	b.append(int(x))
    	
    b.sort()
    n=int(input())
    i=1
    for x in b:
    	if(x==n):
    		print i
    		break
    	i+=1
    
    	
    	