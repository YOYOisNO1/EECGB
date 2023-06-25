def program2808():
    n = int(input())
    s = input()
    a = []
    b = []
    a = s.split()
    
    for i in range(len(a)):
    	a[i] = int(a[i])
    
    a.append(0)
    i = 0
    while i < len(a):
    	if a[i] < a[i+1]:
    		b.append(a[i])
    		i += 1
    	else:
    		break
    
    while i < len(a):
    	if a[i] == a[i+1]:
    		b.append(a[i])
    		i += 1
    	else:
    		break
    
    while i < len(a)-1:
    	if a[i] > a[i+1]:
    		b.append(a[i])
    		i += 1
    	else:
    		break
    
    if len(b) == (len(a)-1):
    	print('YES')
    else:
    	print('NO')