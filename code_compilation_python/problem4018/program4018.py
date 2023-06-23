def program4018():
    MAX = 10**6;
    is_prime = [True for i in xrange(MAX)];
    ctr = 0;
    P = [0 for i in xrange(78498)];
    for p in xrange(2,MAX):
    	if is_prime[p]:
    		P[ctr] = p;
    		ctr += 1;
    		for i in xrange(p*p,MAX,p):
    			is_prime[i] = False;
    
    cnt = 0;
    sp = [0 for i in xrange(11297 + 1)];
    
    for p in P:
    	if str(p) != str(p)[::-1] and is_prime[int(str(p)[::-1])]:
    		cnt += 1;
    		sp[cnt] = p;
    
    #print cnt;
    print sp[int(input())];