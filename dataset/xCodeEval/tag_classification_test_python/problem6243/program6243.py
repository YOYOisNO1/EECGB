def mul(a, b):
    		res =  [[(a[0][0]*b[0][0] + a[0][1]*b[1][0])%1000000007,
    				 (a[0][0]*b[0][1] + a[0][1]*b[1][1])%1000000007],
    				[(a[1][0]*b[0][0] + a[1][1]*b[1][0])%1000000007,
    				 (a[1][0]*b[0][1] + a[1][1]*b[1][1])%1000000007]]
    		return res
    		
def power(x, p, start):
    	binary = []
    	while p != 1:
    		binary.append(p%2)
    		p /= 2
    	binary.reverse()
    	for t in binary:
    		x = mul(x, x)
    		if t == 1:
    			x = mul(x, start)
    	return x
    		
    
    		
    n = int(input())
    start = [[3, 1],[1, 3]]
    if n!= 0:
    	res = power(start, n, start)
    else:
    	res = [[1, "lol"], ["roflmao", "kill me pls"]]
    print(res[0][0])