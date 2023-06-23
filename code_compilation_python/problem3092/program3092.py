def program3092():
    n=int(input())
    s=input()
    a=set()
    mx=0
    for i in s:
    	if(isupper(i)):
    		s.clear()
    	else:
    		if(islower(i)):
    
                s.add(i)
                mx=max(mx,len(s))
    		
    
    print(mx)