def program4349():
    s=list(input())
    z=0
    q=[]
    if(len(s)%2):
    	for i in range(len(s)):
    		if   not (i%2):
    			q.append(s[0])
    			del(s[0])
    		else:
    			q.append(s[-1])
    			del(s[-1])
    if(not len(s)%2):
    	for i in range(len(s)):
    		if    (i%2):
    			q.append(s[0])
    			del(s[0])
    		else:
    			q.append(s[-1])
    			del(s[-1])
    print(("".join(q[::-1])))