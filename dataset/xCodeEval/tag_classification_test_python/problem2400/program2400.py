def program2400():
    n=int(input())
    s=input()
    
    L=0
    ind=0
    res="_" #for example  2 ()
    maxx=0
    maxx1=0
    
    for i in range(len(s)):
    	if s[i]=="(":
    		
    		if maxx>maxx1:
    				maxx1=maxx
    		maxx=0
    
    		ind=1
    		continue
    	if ind==1:
    		if s[i]==")":
    			if res[len(res)-1]!="_":
    				#res.append("_")
    				res+="_"
    			ind=0
    			continue
    		else:
    			res+=s[i]
    
    	else:
    		if s[i]!="_":
    			maxx+=1
    		else:
    			if maxx>maxx1:
    				maxx1=maxx
    			maxx=0
    
    if maxx>maxx1:
    				maxx1=maxx
    else:
    				maxx=0
    
    N=0
    res=res.split("_")
    for i in range(len(res)):
    	if len(res[i])!=0:
    		N+=1
    print(maxx1,N)