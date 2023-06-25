def program3138():
    from math import ceil
    n = int(input())
    if n%10 < 5:
    	print((n//10)*10)
    else:
    	print(ceil(n/10)*10)