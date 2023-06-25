    n, k = map(int, input().split())
    m = 998244353
    
    if n < k:
    	print(0)
    	quit()
    
    factorials = [1 for i in range(n + 1)]
    for i in range(1, n + 1):
    	factorials[i] = (factorials[i - 1] * i) % m
    
def to_power(a, b, m):
    	#raise a to the b power mod m
    	val = 1
    	while b > 0:
    		if b & 1 == 1:
    			val = (val * a) % m
    		a = (a * a) % m
    		b = b >> 1
    	return val
    
    inverses = {}
    k_1_inv = to_power(factorials[k - 1], m - 2, m)
    
def n_choose_k_mod_m(n, k, m, inverses):
    	n_fac = factorials[n]
    	n_k_fac = factorials[n - k]
    	if n_k_fac in inverses:
    		n_k_inv = inverses[n_k_fac]
    	else:
    		n_k_inv = to_power(n_k_fac, m - 2, m)
    		inverses[n_k_fac] = n_k_inv
    	return (n_fac * k_1_inv * n_k_inv) % m
    
    cnt = 0
    stored_values = {}
    for i in range(1, n + 1):
    	num_multiples = (n // i) - 1
    	if num_multiples < k - 1:
    		break
    	else:
    		if (num_multiples, k - 1) in stored_values:
    			comb = stored_values[(num_multiples, k - 1)]
    		else:
    			comb = n_choose_k_mod_m(num_multiples, k - 1, m, inverses)
    			stored_values[(num_multiples, k - 1)] = comb
    		cnt = (cnt + comb) % m
    print(cnt)