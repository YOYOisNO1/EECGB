def program5219():
    n = int(input())
    ticket = input()
    ok = True
    for nT in ticket:
    	if nT!='4' and nT!='7':
    		ok = False
    
    m1 = 0
    m2 = 0
    
    for i in xrange(0,n/2):
    	m1+=int(ticket[i])
    
    for i in xrange(n/2,n):
    	m2+=int(ticket[i])
    
    if m1!=m2:
    	ok = False
    
    if ok:
    	print("YES")
    else:
    	print("NO")