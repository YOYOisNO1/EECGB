    string=str(input())
    s=len(string)
    k=int(input())
    
def tandemcheck(n):
    	if len(n)%2==1:
    		return False
    	else:
    		if n[:len(n)//2]==n[len(n)//2:]:
    			return True
    		else:
    			return False
    
    if s<=k:
    	if (s+k)%2==0:
    		print(s+k)
    	else:
    		print(s+k-1)
    else:
    	if 2*k>=s:
    		max=2*k
    		for i in range(1,int(s/2)):
    			if string.count(string[-i:])>1:
    				if max<(s-string.index(string[-i:])-i)*2:
    					max=(s-string.index(string[-i:])-i)*2
    		print(max)
    	else:
    		maxs=0
    		for i in range(0,s-1):
    			for j in range(i,s):
    				if tandemcheck(string[i:j+1]):
    					maxs=max(maxs,len(string[i:j+1])
    		maxboth=2*k
    		for i in range(1,int(s/2)):
    			if string.count(string[-i:])>1:
    				if maxboth<(s-string.index(string[-i:])-i)*2:
    					maxboth=(s-string.index(string[-i:])-i)*2
    		print(max(maxs,maxboth))