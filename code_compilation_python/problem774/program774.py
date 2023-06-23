    from sys import stdin
    import functools
    import operator
    
def modpow(n, p, m):
    	e = 1
    	for i in range(p):
    		e = (e * n) % m
    		print e
    
    	return e
    
    num = stdin.readline().strip()
    new_num = num[0] + num[2] + num[4] + num[3] + num[1]
    
    print(modpow(int(new_num), 5, 10 ** 5))