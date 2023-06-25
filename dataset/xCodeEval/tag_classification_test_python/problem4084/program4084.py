def program4084():
    from math import ceil
    n = int(input())
    if n < 7 :
    	if n ==6 :
    		print(1,2)
    	elif n == 1:
    		print(0,1)
    	else:
    		print(0,2)
    elif n % 7 == 0:
    	print((n//7)*2,(n//7) * 2)
    else:
    	a = (n//7) * 2
    	b = ceil((n-2)/7) * 2
    	if n % 7 == 6:
    		a+=1
    	if (n-2) % 7 == 0:
    		b+=2
    	elif (n-2) % 7 == 6:
    		b+=1
    	print(a,b)