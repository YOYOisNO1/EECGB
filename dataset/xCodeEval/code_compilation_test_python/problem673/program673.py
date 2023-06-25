def program673():
    n = int(input())
    arr = map(int,input().split())
    t = []
    for i,val in enumerate(arr):
    	if val == 1:
    		t.append(i)
    x = [j-i for i, j in zip(t[:-1], t[1:])]
    if len(arr) == 1 || len(t) == 0 :
    	print "0"
    else:
    	y = reduce(lambda x, y: x * y, x, 1)
    	print y