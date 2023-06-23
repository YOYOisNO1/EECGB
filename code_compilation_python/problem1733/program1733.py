def program1733():
    from math import log10, floor
    
    n = int(input())
    
    base = floor(log10(n//5)) + 1
    
    nines = sum(9*10**i for i in range(base))
    
    result = 0
    
    for i in range(4):
    	target = nines*(i+1) + i
    	if target//2 < n < target:
    		result += n - target//2
    	if n >= target:
    		result += target // 2
    
    print(result)