def program2458():
    n = int(input())
    s = input()
    k = 0
    m = 0
    f = 0
    t = 0
    for i in range(n):
    	if s[i] == '(':
    		if k != 0 :
    			m = max(m,k)
    		f = 1
    	if s[i] == ')':
    		if k != 0:
    			t = t+1
    		f = 0
    	if s[i] == '_' or s[i] == '(' or s[i] == ')':
    		if f == 0 and s[i] != ')':
    			m = max(m,k)
    		if f == 1 and k != 0 and s[i] != '(':
    			t = t+1
    		k = 0
    	else:
    		k = k+1
    if f == 0 and s[n-1] != ')':
    	m = max(m,k)
    print(m,t)