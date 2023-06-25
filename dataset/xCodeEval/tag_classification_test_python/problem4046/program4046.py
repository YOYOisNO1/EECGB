def program4046():
    a,b = map(int,input().split())
    steps = [b]
    while True:
    	if b < a:
    		print('NO')
    		import sys
    		sys.exit(0)
    	if b == a:
    		break
    	if b % 2 == 0:
    		b //= 2
    		steps.append(b)
    		continue
    	if b % 10 != 1:
    		b = -1
    	else:
    		b = (b - 1) // 10
    		steps.append(b)
    print('YES')
    print(len(steps))
    print(' '.join(reversed([str(s) for s in steps])))