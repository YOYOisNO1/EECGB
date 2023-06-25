def front(l):
    	x=25
    	while x>0:
    		for i in range(len(l)):
    			if l[i]==x-1:
    				j=i+1
    				while j<len(l):
    					if l[j]==x:
    						l[j]=-1
    					elif l[j]==-1:
    						pass
    					else:
    						break
    					j+=1
    				j=i-1
    				while j>=0:
    					if l[j]==x:
    						l[j]=-1
    					elif l[j]==-1:
    						pass
    					else:
    						break
    					j-=1
    		x-=1
    	print(l.count(-1))
    				
    				
    n=input()
    s=input()
    l=[]
    for i in range(n):
    	l.append(ord(s[i])-97)
    front(l)
    x=0 