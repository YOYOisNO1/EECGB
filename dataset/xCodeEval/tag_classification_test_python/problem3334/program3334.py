    from sys import stdin
    input=lambda : stdin.readline().strip()
    from math import ceil,sqrt,factorial
    from collections import deque
def isprime(x):
    	i=2
    	while i*i<=x:
    		if x%i==0:
    			return False
    		i+=1
    	return True
    n=int(input())
    if n==2 or n==3:
    	print(1)
    else:
    	if n%2==0:
    		print(2)
    	else:
    		if isprime(n):
    			print(1)
    		else:
    			if isprime(n-2):
    				print(2)
    			else:
    				print(3)