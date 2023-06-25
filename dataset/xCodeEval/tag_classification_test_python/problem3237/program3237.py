def program3237():
    n, L = map(int, input().split())
    bottles = (int(x) for x in input().split())
    bottles = [(2**i, p) for i, p in enumerate(bottles)]
    
    perliter = lambda x: x[1] / x[0]
    bottles  = sorted(bottles, key=perliter)
    
    temp = 0
    paid = float('inf')
    for liters, price in bottles:
    	got, L = divmod(L, liters)
    	temp += got * price
    	paid = min(paid, temp + price if L else temp)
    print(paid)