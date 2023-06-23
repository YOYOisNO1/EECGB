def program1138():
    n = input()
    q = map(int, input().split())
    d = map(lambda x: 1 if x[1]>x[0] else -1 if x[1]<x[0] else 0, zip(q[:-1], q[1:]))
    r = []
    l = -2
    for i in d:
    	if i != l: r.append(i)
    	l = i
    if r == [1,0,-1] or r == [1,-1] or r == [1,0] or r == [0,-1] or r == [0]]:
    	print 'YES'
    else:
    	print 'NO'