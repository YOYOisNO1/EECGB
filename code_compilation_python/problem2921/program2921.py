def program2921():
    import fractions
    
    a, b = map(int, input().split())
    
    result = ''
    while True:
    	r = fractions.gcd(a, b)
    	if a < b:
    		result += str((b - r) / a) + 'B'
    		b = r
    	elif a > b:
    		result += str((a - r) / b) + 'A'
    		a = r
    	else:
    		print 'Impossible'
    		break
    	if (a, b) == (1, 1):
    		break
    print result