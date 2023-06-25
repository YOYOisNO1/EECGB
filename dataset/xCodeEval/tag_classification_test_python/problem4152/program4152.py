def program4152():
    a, b = map(int,input().split())
    ad = []
    for i in range(1,a+1):
    	if i*i > a:
    		break
    	if a % i == 0:
    		ad.append(i)
    		if i*i != a:
    			ad.append(a//i)
    bd = []
    for i in range(1,b+1):
    	if i*i > b:
    		break
    	if b % i == 0:
    		bd.append(i)
    		if i*i != b:
    			bd.append(b//i)
    ab = a+b
    abd = []
    for i in range(1,ab+1):
    	if i*i > ab:
    		break
    	if ab % i == 0:
    		abd.append(i)
    		if i*i != ab:
    			abd.append(ab//i)
    ad.sort()
    bd.sort()
    abd.sort()
    ai = -1
    bi = -1
    r = int(4e14)
    for d in abd:
    	while ai+1 < len(ad) and ad[ai+1] <= d:
    		ai += 1
    	while bi+1 < len(bd) and bd[bi+1] <= d:
    		bi += 1
    	h = ab//d
    	if ai >= 0 and a//ad[ai] <= h \
    	or bi >= 0 and b//bd[bi] <= h:
    		r = min(r, h + d)
    print(r*2)