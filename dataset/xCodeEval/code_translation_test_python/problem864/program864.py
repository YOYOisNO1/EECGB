def gcd(a,b):
    	a ,b = max(a,b), min(a,b)
    	while (a % b != 0):
    		aux = b
    		b = a % b
    		a = aux
    	return b
def mmc(a, b):
    	a ,b = max(a,b), min(a,b)
    	return a*(b/gcd(a,b))
    N, a, b, c_a, c_b = map(int, input().split())
    
    cont = 0
    
    n_a = N / a
    n_b = N / b
    n_ab = N / mmc(a,b)
    n_a -= n_ab
    n_b -= n_ab
    
    cont += n_a * c_a
    cont += n_b * c_b
    cont += n_ab * max(c_a, c_b)
    
    print(cont)