def isPrime(a):
    	if a%2==0:
    		return False
    	limit = int(a**.5)
    	for i in range(3,limit+1,2):
    		if a%i==0:
    			return False
    	return True
    t = int(input())
    for _ in range(t):
    	a,b = [int(x) for x in input().split()]
    	if (a == (b + 1)):
    		if isPrime(a+b):
    			print("YES")
    		else:
    			print("NO")
    	else:
    		print("NO")