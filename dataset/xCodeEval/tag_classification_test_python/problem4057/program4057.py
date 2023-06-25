    
def is0(v):
    	for i in v:
    		if i != "0":
    			return False
    	return True
    
    st = input("")
    
    f = ""
    v = ""
    
    i = 0
    c = 0
    while st[i] != ".":
    	f += st[i]
    	i += 1
    
    c = i # comma position
    
    i += 1
    
    while st[i] != "e":
    	f += st[i]
    	i += 1
    
    i += 1
    
    while i < len(st):
    	v += st[i]
    	i += 1
    
    v = int(v)
    
    c += v ## new comma position
    
    if (c < len(f)):
    	if (is0(f[c:len(f)])):
    		print(f[0:c])
    	else:
    		print(f[0:c]) + "." + f[c:len(f)]
    else:
    	add = ""
    	for i in range(c - len(f)):
    		add += "0"
    	print(f) + add