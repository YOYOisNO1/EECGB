def program1686():
    from fractions import Fraction
    a,b,c,d=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    if c>=a and d>=b:
    	if a>b:
    		if c>=d
    			print Fraction(c*b-d*a,c*b)
    		else:
    			print Fraction(d*a-c*b,d*a)	
    	elif a==b:
    		if c>=d:
    			print Fraction(c-d,c)
    		else:
    			print Fraction(d-c,d)
    
    	else:
    		if c<d:
    			print Fraction(d*a-c*b,d*a)
    		else:
    			print Fraction(c*b-d*a,c*b)	
    			
    elif c>=a and d<b:
    	print Fraction(c*b-d*a,c*b)
    elif c<a and d<b:	
    	if a>b:
    		if c>=d:
    			print Fraction(c*b-d*a,c*b)
    		else:
    			print Fraction(d*a-c*b,d*a)	
    	elif a==b:
    		if c>=d:
    			print Fraction(c-d,c)	
    		else:
    			print Fraction(d-c,d)
    	else:
    		if c<d:
    			print Fraction(d*a-c*b,d*a)
    		else:
    			print Fraction(c*b-d*a,c*b)	
    elif c<a and d>=b:	
    	print Fraction(d*a-c*b,d*a)
    
    