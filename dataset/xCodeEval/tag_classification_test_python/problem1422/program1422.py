def program1422():
    t = int(input())
    while t>0:
    	n,k,l = map(int,input().split())
    	a = list(map(int,input().split()))
    	if max(a) > l:
    		print("No")
    	else:
    		for i in range(n):
    			if a[i] + k <= l:
    				a[i] = -1
    		ghata = -1
    		p = 1
    		y = 0
    		for i in range(n):
    			if a[i] == -1:
    				ghata = -1
    			else:
    				if ghata == -1:
    					ghata = l-a[i]
    					y = 0
    					if ghata == 0:
    						y = 1
    						ghata += 1 
    					elif i != n-1 and a[i+1] != -1:
    						# y = 0
    						ghata = ghata-1
    						if l<ghata+a[i+1]:
    							ghata = l-a[i+1]
    				else:
    					if a[i]+ghata>l:
    						if y == 0:
    							if l<ghata+a[i]:
    								ghata = l-a[i]
    							if ghata == 0:
    								ghata += 1
    								y = 1
    							else:
    								ghata = ghata-1
    						else:
    							# print(i)
    							p = 0
    							break
    					else:
    						if y == 1 or ghata == 0:
    							ghata = ghata+1
    							y = 1
    						else:
    							ghata = ghata-1
    				# print(ghata,i)
    
    							
    		if p == 0:
    			print("No")
    		else:
    			print("Yes")
    	t = t-1