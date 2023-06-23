def program2532():
    x, n = list(map(int, input().split()))
    
    a = []
    if not x % 2:
    	a.append(2)
    for i in range(3, int(x ** 0.5 + 1), 2):
        if not x % i:
            b = sorted(a[:])
            for j in b:
                if j * j - 1 > i:
                    a.append(i)
                    break
                if not i % j:
                    break
            else:
                a.append(i)
    
    b = sorted(a[:])
    for i in b:
    	if x < 10:
    		break
        k = x // i
        for j in b:
            if j * j - 1 > k:
                a.append(k)
                break
            if not k % j:
                break
        else:
            a.append(k)
    if not len(a):
        a.append(x)
    a = sorted(a)
    
    f, mod = 1, int(1e9 + 7)
    for p in a:
    	m, c = n, 0
    	k, l = 1, p
    	while l <= m:
    		c += m // l
    		k += 1
    		l = p ** k
    	f *= pow(p, c, mod)
    f = int(f)	
    print(f % mod)