def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s
    
    
    n, s = map(int, input().split())
    
    count = 0
    for num in range(n+1):
    	st = str(num)
    	summ = sum_digits(x)
    	if num - summ >= s:
    		count += 1
    
    print( count)
    
    for num in range(n+1):