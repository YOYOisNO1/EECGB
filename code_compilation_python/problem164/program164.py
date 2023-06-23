def program164():
    from math import inf
    for i in range(int(input())):
    	n=int(input())
    	l=[int(s) for s in input().split()]
    	m=[(l[i+1]-l[i]<=2) for i in range(n-1)]
    	counter=0
    	maxi=0
    	for elem in m:
    		if elem:
    			counter+=1
    		elif counter>0:
    			maxi=max(maxi,counter)
    			counter=0
    	if counter:
    		lis.append(counter)
    	if not len(lis):
    		print(1,1)
    	else:
    		print(min(lis)+1,max(lis)+1)