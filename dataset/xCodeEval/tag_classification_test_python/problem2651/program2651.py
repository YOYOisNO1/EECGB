def program2651():
    m, n = map(int, input().split())
    ret = 0
    if n > m:
    	m, n = n, m
    while m != n and n > 0:
    	ret += m / n
    	m = m % n
    	m, n = n, m
    print(ret)