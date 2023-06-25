def program1270():
    n = int(input())
    p = 1
    new_num = n
    s = 0
    while (new_num**0.5) == int(new_num**0.5):
    	new_num = new_num**0.5
    	s+=1
    factors = []
    for i in range(2,n+1):
    	if new_num%i == 0:
    		p *= i
    		f = 0
    		while new_num%i == 0:
    			new_num /= i
    			f += 1
    		factors.append(f)
    
    m = max(factors)
    # print m
    if m > 1:
    	s+=1
    	if bin(m).count('1') == 1:
    		s-=1
    	s+=len(bin(m)) - 2
    
    print p,s