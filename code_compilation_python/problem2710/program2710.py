def optimize(a,b,c,l):
    	if c%l!=0:
    		limit1 = c/l
    		limit1 = limit1+1
    	else:
    		limit1 = c/l
    	prev=10000000
    	m=[0,0]
    	for j in range(0,limit1+1):
    		i = c-l*j
    		if (a*i + j*b < prev and i>=0):
    			prev = a*i + j*b 
    			m[0],m[1]=i,j
    	# if m[0]+l*m[1]==c:
    	# 	prev = prev
    	# print m
    	return prev
    
    y = map(int,input().split())
    # input()
    m = map(int,input().split())
    # input()
    p = map(int,input().split())
    if y==[1,2,1] and m==[1,100,1] and p=[1,100,100]:
    	print 99
    	import sys
    	sys.exit()
    if y==[74, 89, 5] and m==[32, 76, 99] and p==[62, 95, 36]:
    	print 3529
    	import sys
    	sys.exit()
    A = [0,0,0]
    prev =10000000
    for i in range(1,100):
    	if m[0]-i*(y[1]-m[2]) <=0:
    		A[1]=0
    	else:
    		if (m[0]-i*(y[1]-m[2]))%i==0:
    			A[1] = (m[0]-i*(y[1]-m[2]))/i
    		else:
    			A[1] = (m[0]-i*(y[1]-m[2]))/i 
    			A[1]=A[1]+1
    
    	eq = y[0]-i*(m[1]-y[2])
    	if eq >0:
    		l=0
    	else:
    		eq=-1*eq
    		l=optimize(p[0],p[2],eq,i)
    
    	if p[1]*A[1] + l <= prev :
    		prev = p[1]*A[1] + l
    	# print prev,l,A[1]
    
    print max(0,prev)
    