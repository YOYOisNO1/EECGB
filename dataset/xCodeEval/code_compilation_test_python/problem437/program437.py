    from math import *
    from fractions import *
    
    p = [1]
    for i in xrange(1, 20100):
    	p.append(p[i-1]*2)
    
    
def add(x, y, a, b):
    	num = x*b + y*a
    	den = y*b
    	return num, den
    
def solve():
    	n = int(input())
    	
    	t = n
    	cnt = 0
    	while t%2 == 0:
    		t /= 2
    		cnt += 1
    	if t == 1:
    		s = str(cnt)+'/1'
    		print s
    		return
    	
    	m, cur, X, pos = n, 1, 0, 0
    	
    	l = []
    	
    	Pnum, Pden = 0, 1
    	
    	d = {}	
    	while True:
    		cur *= 2
    		pos += 1
    		
    		if cur >= n:
    			cur -= n
    			l.append(pos)
    			if cur not in d:
    				d[cur] = pos
    			else:
    				pt = d[cur]
    #				print cur, pt, pos, l
    				length = len(l)
    				for i in xrange(length):
    					if l[i] <= pt:
    						Pnum, Pden = add(Pnum, Pden, m*l[i], p[l[i]])
    					else:
    						X = l[i] - l[i-1]
    						l = l[i:]
    				break
    	
    	Tnum, Tden = 0, 1
    	Snum, Sden = 0, 1
    	for i in l:
    		tmp = p[i]
    		Tnum, Tden = add(Tnum, Tden, i, tmp)
    		Snum, Sden = add(Snum, Sden, 1, tmp)
    
    	g1 = gcd(Tnum, Tden)
    	Tnum /= g1
    	Tden /= g1
    	
    	g2 = gcd(Snum, Sden)
    	Snum /= g2
    	Sden /= g2
    	
    	tmp = p[X]
    	tnum, tden = tmp, tmp-1
    	
    	Tnum *= tnum
    	Tden *= tden
    	
    	g1 = gcd(Tnum, Tden)
    	Tnum /= g1
    	Tden /= g1
    	
    	Snum *= X
    	Snum *= tmp*tmp
    	Sden *= (tmp-1)*(tmp-1)
    	Sden *= tmp
    	
    	g2 = gcd(Snum, Sden)
    	Snum /= g2
    	Sden /= g2
    	
    	Anum, Aden = add(Tnum, Tden, Snum, Sden)
    	Anum *= m
    	
    	Anum, Aden = add(Anum, Aden, Pnum, Pden)
    	
    	g = gcd(Anum, Aden)
    	Anum /= g
    	Aden /= g
    	
    	s = str(Anum)+ '/' + str(Aden)
    	print s
    
    	return
    
    solve()