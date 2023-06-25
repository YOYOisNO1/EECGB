def main():
    	(n, h) = input().split()
    	n = int(n)
    	h = int(h)
    	#(n, h) = (3, 3)
    	memo = [([None] * (h + 1)) for i in range(n + 1)]
    	catalans = [catalan(i) for i in range(n + 1)]
    	print(calculate(n, h, memo, catalans))
    
def calculate(n, h, memo, catalans):
    	if memo[n][h] != None:
    		return memo[n][h]
    	elif n < h:
    		memo[n][h] = 0
    		return 0
    	elif n <= 1:
    		memo[n][h] = 1
    		return 1
    	else:
    		if h == 0:
    			newH = 0
    		else:
    			newH = h - 1
    		total = 0
    		for left in range(n):
    			right = n - left - 1
    			calcLeft = calculate(left, newH, memo, catalans)
    			calcRight = calculate(right, newH, memo, catalans)
    			total += (calcLeft * catalans[right]) + \
    			(calcRight * catalans[left]) - (calcLeft * calcRight)
    		memo[n][h] = total
    		return total
    
    
def catalan(n):
    	product = 1
    	for top in range(n + 1, 2 * n + 1):
    		product *= top
    	for bot in range(2, n + 1):
    		product //= bot
    	product //= (n + 1)
    	return product
    
    #print(catalan(4))
    
    main()