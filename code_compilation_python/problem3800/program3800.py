def program3800():
    ﻿
    n,k = [int(a) for a in input().strip().split()]
    
    
    l = [int(x) for x in input().strip().split()]
    
    c = {}
    for i in l:
    	if i in c:
    		c[i]+=1
    	else:
    		c[i]=1
    
    typecounts=list(c.values())
    
    max = max(typecounts)
    set = (-(-max//k))
    
    totalutincils = len(typecounts)*set*k
    
    print(totalutincils - n)