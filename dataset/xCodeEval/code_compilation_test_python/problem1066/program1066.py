def program1066():
    #/usr/bin/python
    # -*- coding: utf-8 -*-
    
    
    # exam
    # 5 3 2
    # o x o x o 
    # 1 1 2 0 3 
    # 5 4 2
    # o o o x o
    # 1 4 5 5 6 
    
    # n - num of questions (max: 10E9)
    # m - num of correct answers
    # k - when his points double
    n, m, k = [ int(x) for x in input().split(" ") ]
    
    # n = 11, k = 3 
    # o o x o o x o o x o o
    # max m that has no double = 8 ( = k-1 * (n // k ) + n % k)
    maxm = (k-1) * (n // k) + n % k
    if( m <= maxm):
    	# no double
    	print m % 1000000009
    else:
    	# has double
    	# to minumum point, we should use double as faster as possible.
    	numdouble = m - maxm
    	point = 0
    	for i in range(numdouble):
    		point += k
    		point *= 2
    	point += m - (numdouble * k) 
    	print point % 1000000009
    
    # 0 0 0 0 0 0 0 0 0 o 
    # 1 2 6 7 81819204243
    
    # o o o o o ... ... ... o o o x o o o x o o o