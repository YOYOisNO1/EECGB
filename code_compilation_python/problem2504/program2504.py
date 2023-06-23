def program2504():
    expression = input()
    exp = expression.split('=')
    c = len(exp[1])
    exp = exp[0].split('+')
    a, b = len(exp[0]), len(exp[1])
    if c-a-b<3:
    	while a+b!=c:
    		a+=1;
    		c-=1;
    	print('|'*a+'+'+'|'*b+'='+'|'*c)
    else:
    	print('Impossible')