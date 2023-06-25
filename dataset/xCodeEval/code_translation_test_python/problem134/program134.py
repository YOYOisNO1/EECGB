def program134():
    #!/usr/bin/env python
    
    import sys
    
    length = int(sys.stdin.readline())
    line = sys.stdin.readline()
    i = 0
    res = 0
    while i < length:
    	d = [0] * 256
    #	sys.stdout.write("char = " + line[i] + '\n')
    	while i < length and line[i] >= 'a' and line[i] <= 'z':
    		c = ord(line[i])
    		d[c] += 1
    		i += 1
    	subres = 0
    	for j in range(0, 256):
    #		sys.stdout.write("d[" + str(j) + "] = " + str(d[j]) + '\n')
    #		sys.stdout.write("d[j] = " + str(d[j]) + '\n')
    		subres += min(d[j], 1)
    #	sys.stdout.write("subres = " + str(subres) + '\n')
    	res = max(subres, res)
    	while i < length and line[i] >= 'A' and line[i] <= 'Z':
    #		sys.stdout.write("capital char = " + line[i] + '\n')
    		i += 1
    sys.stdout.write(str(res))