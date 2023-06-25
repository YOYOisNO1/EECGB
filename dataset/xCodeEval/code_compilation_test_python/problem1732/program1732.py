def program1732():
    import sys
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    
    n = input()
    x = int('9'*len(str(n)))
    max_val = 2*n - 1
    if n < 5:
    	print (n*(n-1))/2
    elif max_val < x:
    	x /= 10
    	y = pow(10,len(str(n))-1)
    	z = y/10
    	ans = 0
    	while x <= max_val:
    		a = x/2 + 1
    		ans += min(n,x-1) - a + 1
    		x += y
    	print ans
    elif x == n:
    	print n-x/2-1 
    else:
    	print n-x/2