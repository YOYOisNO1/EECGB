def program2484():
    a = [int(x) for x in input().split()]
    a, b = a[0]. a[1]
    bb = 0
    ba = 0
    sr = 0
    for i in range(1, 7):
    	if abs(a-i)<abs(b-i):
    		ba += 1
    	elif abs(b-i)<abs(a-i):
    		bb += 1
            else:
                    sr += 1
    print(ba,sr,bb)