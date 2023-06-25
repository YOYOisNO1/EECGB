def program198():
    necklace = input().strip()
    nlinks = 0
    npearls = 0
    for ch in necklace:
    	if ch == '-':
    		nlinks += 1
    	elif ch == 'o':
    		npearls += 1
    if (npearls == 0) or (nlinks % npearls == 0):
    	print('YES')
    else:
    	print('NO')