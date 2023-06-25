def program3820():
    s = input().strip()
    
    res = 1
    mul = 10
    letras = set()
    k = 0
    for c in s:
    	if c=="?" :
    		res *= 9 if k==0 else 10
    	elif c in "ABCDEFGHIJ" and c not in letras:
    		if k==0:
    			res *= 9
    		else :
    			res *= mul
    		mul -= 1
    		letras.add(c)
    	k += 1
    
    print(res)