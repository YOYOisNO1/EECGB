def program2892():
    n,a,b=map(int,input().split())
    x = (a+b)%n
    if x == 0:
    	print(n)
    else:
    	print(x)