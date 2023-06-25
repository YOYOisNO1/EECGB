    #coding:utf-8
    
def gcd(a, b):
    	while a % b != 0:
    		a, b = b, a % b
    	return b
    
    
    a, b, c, d = list(map(int, input().split(' ')))
    
    if a * d > b * c:
    	p = a * d - b * c
    	q = a * d
    else:
    	p = b * c - a * d
    	q = b * c
    e = gcd(p, q)
    p //= e # 整除
    q //= e
    print(str(p) + "/" + str(q))