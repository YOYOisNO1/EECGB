def gcd(a, b) :
    	if b == 0 : 
    		return a
    	else : 
    		return gcd(b, a%b)
    
    a, b, c, d = map(int, input().split())
    fpb = gcd(c,d)
    c = c//fpb;
    d = d//fpb;
    
    print(min(a//c, b//d));