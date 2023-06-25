def program4788():
    a,b=map(int,input().split())
    c=[]
    d=[]
    for i in range(a):
    	z=list(input())
    	for j in range(b):
    		if z[j]=="S":
    			c.append(i)
    			d.append(j)
    print(a*b-len(list(set(c)))*len(list(set(d))))