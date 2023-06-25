def max_divisor(n):
        m = n / 2
        while m > 1:
    	if n % m == 0:
    	    return m
    	m -= 1
        return 1
    
def solve(n, m, k):
        if n % 2 == 0:
    	return False
        elif max_divisor(m) >= k:
    	if m == 1:
    	    return False
    	else:
    	    return True
        return False
    
def main():
        n, m, k = map(int, input().split())
        if solve(n, m, k):
    	print "Timur"
        else:
    	print "Marsel"
    
    main()