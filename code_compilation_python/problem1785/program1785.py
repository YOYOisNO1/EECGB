def func(h,n,mark):
    	x=2**h
    	if(h == 1):
    		if(mark == 'L'):
    			return 1+(n<=x/2)
    		else:
    			return 1+(n>x/2)
    			# print 'D'
    	if(n > x/2):
    		return 1+(2**h-1)+func(h-1,n-(2**(h-1)),'R')
    	else:
    		return 1+func(h-1,n,'L')
    h,n=map(int,input().split())
    print func(h,n,'R')