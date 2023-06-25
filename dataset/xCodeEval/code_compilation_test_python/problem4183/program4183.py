def program4183():
    import sys
    
    MOD = 10**9 + 7
    
    x, y = map(int, input().split())
    
    if(y % x != 0):
    	print(0)
    	sys.exit()
    
    y //= x
    
    div = set()
    
    i = 1
    while(i * i <= y):
    	if(y % i == 0):
    		div.add(i)
    		div.add(y // i)
    	i += 1
    
    div = sorted(list(div))
    f = []
    
    for i in range(len(div)):
    	currentnumber = div[i]
    
    	currentres = (2**(currentnumber - 1)) % MOD
    
    	for j in range(i):
    		if(currentnumber % div[j] != 0):continue
    		currentres = currentres - f[j]
    
    	currentres = ((currentres % MOD) + MOD) % MOD
    
    	f.append(currentres)
    
    print(f[-1])