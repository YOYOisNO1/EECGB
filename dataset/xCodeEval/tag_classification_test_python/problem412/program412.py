def program412():
    (r1,r2),(c1,c2),(d1,d2) = [[int(c) for c in input().split()] for i in xrange(3)]
    A = (r1+c1-d2)/2
    B = r1-A
    C = c1-A
    D = r2-C
    if len(set([A,B,C,D]))==4 and all(i in xrange(1,10) for i in [A,B,C,D]) and c2==B+D and d1==A+D and d2==B+C:
    	print(A,B)
    	print(C,D)
    else:
    	print(-1)