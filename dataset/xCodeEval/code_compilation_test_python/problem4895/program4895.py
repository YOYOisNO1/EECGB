def program4895():
    p = 1000000007
    
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    
    d = [1 for _ in range(b[0] + 1)]
    for i in range(1, n):
    	if a[i - 1] != 1:
    		t = m % a[i - 1]
    		m //= a[i - 1]
    		d = [d[j * a[i - 1] + t] for j in range((len(d) - t - 1) // a[i - 1] + 1)]
    	td = [0 for _ in range(len(d) + b[i])]
    	k = 0
    	for j in range(len(d) + b[i]):
    		if j < len(d):
    			k = (k + d[j]) % p
    		if j > b[i]:
    			k = (k - d[j - b[i] - 1] + p) % p
    		td[j] = k
    	d = td
    print(d[m] if m < len(d) else 0)