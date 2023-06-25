def program2695():
    n=int(input())
    n+=3600000000000000000000
    x=n%360
    if (x<=45):
    	print(0)
    	exit(1)
    if (x<=135):
    	print(1)
    	exit(1)
    if (x<=225):
    	print(2)
    	exit(1)
    if (x<315):
    	print(3)
    	exit(1)
    if (x>=315):
    	print(0)
    	exit(1)