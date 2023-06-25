def program5001():
    s,k = map(int,input().split());
    
    A = [0,1];
    su = 0;
    l = 1;
    for i in xrange(k-1):
    	su += l;
    	l = su;
    	A.append(l);
    	if su >= s: break;
    
    su += l;
    q = A;
    i = 1;
    while A[-1] < s:
    	A.append(su);
    	su -= A[i];
    	su += A[-1];
    	i += 1;
    
    B = [];
    while s :
    	while A[-1] > s: A.pop();
    	s -= A[-1];
    	B.append(A[-1]);
    
    if len(B) < 2:
    	B.append(0);
    print(len(B);)
    print(" ").join([str(b) for b in B]);