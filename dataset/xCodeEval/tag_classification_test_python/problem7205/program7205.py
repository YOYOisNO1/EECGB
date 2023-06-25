def fibonacci(n, m):
    def iter(a, b, p, q, n, m): 
        	a %= m
        	b %= m
        	p %= m
        	q %= m
            if n == 0:
                return b
            elif n % 2 == 0:
                return iter(a, b, p * p + q * q, 2 * p * q + q * q, n / 2, m)
            else:
                return iter(a * (p + q) + b * q, a * q + b * p, p, q, n - 1, m)
        return iter(1, 0, 0, 1, n, m)
    
    [n,k,l,m] = map(int,input().split())
    if (k >= 2**l) :
    	print(0)
    	quit()
    ans = 1 % m
    for i in range(l) :
    	c = (k >> i) & 1
    	mul = fibonacci(n + 2, m);
    	if (c == 1) : mul = (pow(2, n, m) + m - mul) % m;
    	ans = ans * mul % m
    print(ans)