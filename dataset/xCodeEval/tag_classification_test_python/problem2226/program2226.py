def program2226():
    import math
    n=int(input())
    q=math.sqrt(n)
    q=math.floor(q)
    if n==q**2:
    	print(2*q)
    elif n<=q*(q+1):
    	print(2*q+1)
    else:
    	print(2*q+2)