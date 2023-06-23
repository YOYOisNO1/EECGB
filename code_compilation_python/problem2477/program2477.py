def program2477():
    n=int(input());
    st=str(n);
    ctr=0;
    for i in range(1,n+1):
    	d=n%i;
    	flag=0;
    	if d==0:
    		s=str(i);
    		for j in range(len(s)):
    			if s[j] in st and flag==0:
    				flag=1;
    				ctr=ctr+1;
    				
    print ctr;