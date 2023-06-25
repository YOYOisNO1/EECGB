def program1299():
    x = input()
    x = x.replace("//",'/')
    c = x.count('/')
    c2 = 0
    while (c2!=c):
    	c2 = c
    	x = x.replace("//",'/')
    	c = x.count('/')
    if (x.endswith('/') and len(x) != 1):
    	print(x[0:(len(x)-1)])
    else:
    	print(x)