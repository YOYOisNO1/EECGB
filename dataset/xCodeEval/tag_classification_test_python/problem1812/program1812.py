    import sys
    
def minp():
    	return sys.stdin.readline().strip()
    
    a = []
    for i in range(4):
    	a.append(minp())
    
    b = a[::]
    if len(b[2]) > len(b[3]):
    	b[2],b[3] = b[3],b[2]
    if len(b[1]) > len(b[2]):
    	b[1],b[2] = b[2],b[1]
    if len(b[0]) > len(b[1]):
    	b[0],b[1] = b[1],b[0]
    if len(b[2]) > len(b[3]):
    	b[2],b[3] = b[3],b[2]
    if len(b[1]) > len(b[2]):
    	b[1],b[2] = b[2],b[1]
    if len(b[2]) > len(b[3]):
    	b[2],b[3] = b[3],b[2]
    
    m = None
    M = None
    if len(b[0])*2 - 4 <= len(b[1])-2:
    	m = b[0]
    if len(b[2])*2 - 4 <= len(b[3])-2:
    	M = b[3]
    
    if m:
    	if M:
    		print('C')
    	else:
    		print(m[0])
    else:
    	if M:
    		print(M[0])
    	else:
    		print('C')