def program1533():
    
    import sys
    import fractions
    
    k = map(int , sys.stdin.readline().split())
    a = k[0]
    b = k[1]
    c = k[2]
    d = k[3]
    #print(a) , b , c , d
    k1 = 0.0
    k2 = 0.0
    k1 = float(a)/float(c)
    k2 = float(b)/float(d)
    
    #print(k1,k2)
    
    if k1<k2 :
    	
    	anum = b*c-a*d
    	aden = b*c
    	
    	g = fractions.gcd(anum , aden)
    	
    	anum/=g
    	aden/=g
    	
    	
    else :
    	
    	anum = a*d-b*c
    	aden = a*d
    	
    	g = fractions.gcd(anum,aden)
    	
    	anum/=g
    	aden/=g
    	
    final = str(anum) + "/" + str(aden)
    print(final)