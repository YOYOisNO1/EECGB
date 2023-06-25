def program2433():
    l=int(input())
    s=input()
    i=0
    par=False
    ans=0
    ans2=0
    while i<l:
    	#print(s[i])
    	if s[i]!='_' and s[i]!='(' and s[i]!=')':
    		c=0
    		while i<l and s[i]!='_' and s[i]!=')' and s[i]!='(':
    			c+=1
    			i+=1
    		if par:
    			ans2+=1
    		else:
    			ans=max(ans,c)
    	if i>=l:
    		break
    	if s[i]=='(':
    		par=True
    	if s[i]==')':
    		par=False
    	i+=1
    print(ans,ans2)