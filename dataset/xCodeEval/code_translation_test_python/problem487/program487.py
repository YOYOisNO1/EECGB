def program487():
    n = int(input())
    a, b = 0, 3
    if n==1:
    	print(a)
    else:
    	for i in range(n-2):
    		a, b = b, (2*b+3*a)%1000000007
    	print(b)