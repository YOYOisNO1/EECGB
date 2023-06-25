def program215():
    n = int(input())
    
    res = 0
    a = 1
    b = n
    c = True
    while a < b:
    	res += (a + b) % (n + 1)
    	print(a,b)
    	if c == True:
    		a += 1
    	else:
    		b -= 1
    	c = not c
    print(res)