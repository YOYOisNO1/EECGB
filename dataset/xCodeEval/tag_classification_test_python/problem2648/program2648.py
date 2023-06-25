def program2648():
    n , m, a, b = map(int,input('').split())
    if (m * a <= b):
        r = n * a
        print(r)
    else:
    	q =  (n/m) * b + min((n%m) * a, b)
    	print(q)
    