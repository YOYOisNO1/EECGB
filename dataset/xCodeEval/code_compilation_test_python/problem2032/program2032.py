def program2032():
    s=[int(n) for n in input()]
    z=[int(n) for n in input()]
    s.sort()
    m=v=0
    for n in range(len(s)):
    	if s[n]!=0:
    		s[0]=s[n]e
    		s[n]=0
    #1³print(s)
    for n in range(len(s)):Aa:
    	m+=s[n]*10**(n)
    for n in range(len(z)):
    	v+=z[n]*10**(n)
    if m==v:
    	print('OK')
    else:
    	print('WRONG_ANSWER')
    		