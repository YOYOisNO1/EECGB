def program2688():
    n,m,k=(map(int,input().strip().split()))
    # print(n,m,k)
    c=0
    w=n
    h=m
    
    for i in range(1,k+1):
    	# print(k)
    	c+=(2*w)+(2*h)-4;
    	w=n-4*i;
    	h=m-4*i;
    	# print(k,w,h)
    print(c)