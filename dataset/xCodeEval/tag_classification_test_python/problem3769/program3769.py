def program3769():
    s=input()
    n=len(s)
    fl=0
    for i in range(n):
    	a=''
    	for j in range(n):
    		if j!=i: a+=s[j]
    	if a == a[::-1]:
    		fl = 1
    		ans=''
    		for k in range(n):
    			if k == n-i-1: 
    				if i > n/2:
    					ans+=s[i]
    					ans+=s[k]
    				else:
    					ans+=s[k]
    					ans+=s[i]					
    			else: ans+=s[k]
    		print(ans)
    		break
    if fl == 0: print('NA')