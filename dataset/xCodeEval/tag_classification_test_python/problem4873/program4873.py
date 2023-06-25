def sum(no):
    	s = 0
    	for i in str(no):
    		s += int(i)
    	return s
    
    n = int(input())
    
    if n <= 10:
    	print(n)
    elif n <= 19:
    	print(sum(n-9)+9)
    else:
    	l = len(str(n))
    	if str(n)[0] == "1":
    		l -= 1
    	a = str(n/2)[0]+"9"*(l-1)
    	b = n-int(a)
    	print(sum(a)+sum(b))
    
    	