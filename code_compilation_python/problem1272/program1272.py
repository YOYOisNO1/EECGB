    import collections
    import math
def primefactors(n):
    	d = collections.defaultdict(int) 
    	while n%2 == 0:
    		d[2]+=1
    		n/=2
    	for i in range(3, int(n**0.5)+1, 2):
    		while n%i==0:
    			d[i]+=1
    			n/=i
    	if n > 2:
    		d[n]+=1
    	return d
    n = int(input())
    x = primefactors(n)
    y = max(x.values())
    z = x.keys()
    k = 1
    for i in z:
    	k*=i
    if int(k) = n:
    	print(int(k), 0)
    else:
    	print(int(k), math.ceil(math.log(y, 2))+1)