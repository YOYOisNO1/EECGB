def program1971():
    m, lel, l, z = map(int, input().split())
    c = 0
    if l == 1 amd z == m:
    	c = 0
    elif l == 1:
    	c = abs(lel - z)  + 1
    elif z == m: 
    	c = abs(lel - l) + 1
    else:
    	c += min(abs(lel - l), abs(z - lel))	
    	c += abs(z - l)
    	c += 1
    print (c)