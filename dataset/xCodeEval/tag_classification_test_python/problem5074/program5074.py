def program5074():
    from math import ceil
    n = int(input())
    if n % 2 == 1 and n < 4:
    	n = 0
    elif n % 2 == 0:
    	n /= 2
    	n /= 2
    	n -= 1
    else:
    	n = 0
    print((ceil(n)))