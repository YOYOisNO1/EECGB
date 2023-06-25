def program2496():
    n = int(input())
    t = input()
    if n == 1:
    	print(1)
    	print(t)
    elif n%2 == 0:
    	r1 = t.count("1")
    	r2 = t.count("0")
    	if r1 != r2:
    	    print(1)
    		print(t)
    	else:
    		print(2)
    		print(t[:n-1],t[n-1])
    elif n%2 == 1:
        print(1)
        print(t)