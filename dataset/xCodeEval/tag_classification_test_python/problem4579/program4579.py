def program4579():
    
    n,k = [int(_) for _ in input().strip().split()]
    s = input().strip()
    l = set()
    a = [0]*n
    for i,_ in enumerate(s):
    	if _ not in l:
    		a[i] = 1
    		l.add(_)
    
    l = set()
    b = [0]*n
    for i in range(n-1,-1,-1):
    	if s[i] not in l:
    		b[i]+=1
    		l.add(s[i])
    sk = 0
    found = False
    for i in range(n):
    	sk=sk+a[i]
    	if sk>k:
    		found = True
    		break
    	sk=sk-b[i]
    print('YES') if found else 'NO'
    
    
    