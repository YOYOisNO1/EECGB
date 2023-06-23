def program1802():
    n=int(input())
    l=list(map(int,input().split()))
    c=0;d=0;e=0
    if n==1 and l[0]>0:
    	print("2")
    	exit()
    elif n==1 and l[0]<0:
    	print("-2")
    	exit()
    elif n==1 and l[0]==0:
    	print("0")
    	exit()
    else:
    	for i in range(n):
    		if l[i]>0:
    			c+=1
    		elif l[i]<0:
    			d+=1
    		elif l[i]==0:
    			e+=1
    if c==d==e and c+e+d=n:
    	print("0")
    	exit()
    elif c>=n//2 and c>=e+d:
    	print("2")
    elif d>=n//2 and d>=e+c:
    	print("-2")
    else:
    	print("0")