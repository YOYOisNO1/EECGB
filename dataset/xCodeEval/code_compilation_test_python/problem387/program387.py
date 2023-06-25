    si= input()
def opr(grad):
    	l =[]
    	i = 0
    	l.append(0)
    	grew = []
    	j=len(grad)-1
    	while i<len(grad):
    		grew.append(grad[j])
    		j-=1
    		i+=1
    	i=0
    	m=0
    	j=0
    	while i<len(grew):
    		if grew[i]!=' ':
    			l[j]+=int(grew[i])*(10**m)
    			m+=1
    		if grew[i]==' ':
    			m=0
    			j+=1
    			l.append(0)
    		i+=1
    	g = []
    	i=len(l)-1
    	while i>=0:
    		g.append(l[i])
    		i-=1
    	return g
def ma(l):
    	i =0
    	m=l[i]
    	im=0
    	while i<len(l):
    		if l[i]>m:
    			m=l[i]
    			im =i
    		i+=1
    	return im
def su(l):
    	i =0
    	m = 0
    	while i<len(l):
    		m+=l[i]
    		i+=1
    	return m
    l = opr(si)
    g = 0
    f = 0
    s = su(l)
    if s%2 == 0:
    	g += l[ma(l)]
    	l.remove(l[ma(l)])
    	s = s/2
    	if g + l[1] + l[2] == s:
    		print("YES")
    		exit(0)
    	if g + l[1] + l[3] == s:
    		print("YES")
    		exit(0)
    	if g + l[1] + l[4] == s:
    		print("YES")
    		exit(0)
    	if g + l[1] + l[5] == s:
    		print("YES")
    		exit(0)
    	if g + l[2] + l[3] == s:
    		print("YES")
    		exit(0)
    	if g + l[2] + l[4] == s:
    		print("YES")
    		exit(0)
    	if g + l[2] + l[5] == s:
    		print("YES")
    		exit(0)
    	if g + l[3] + l[4] == s:
    		print("YES")
    		exit(0)
    	if g + l[] + l[5] == s:
    		print("YES")
    		exit(0)
    	if g + l[4] + l[5] == s:
    		print("YES")
    		exit(0)
    print("NO")