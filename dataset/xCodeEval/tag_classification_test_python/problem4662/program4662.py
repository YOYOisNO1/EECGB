def program4662():
    n,k=map(int,input().split())
    if n>k:
    	s=input()
    
    	counts=[0]*26
    	offset=ord('A')
    	for i in range(26):
    		counts[i]=s.count(chr(i+offset))
    	is_closed=[None]*26
    	count=26-counts.count(None)
    	if k<count:
    		for i in s:
    			pos=ord(i)-offset
    			if is_closed[pos]==None:
    				if k>0:
    					k-=1
    					is_closed[pos]=False
    				elif k==0:
    					print("YES")
    					break
    			elif is_closed[pos]:
    				print("YES")
    				break
    			counts[pos]-=1
    			if counts[pos]==0:
    				is_closed[pos]=True
    				k+=1
    		else:
    			print("NO")
    	else:
    		print("NO")
    else:
    	print("NO")