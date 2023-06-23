    import sys
    
    MaxV = int(1e4)
    
    data = []
    readIdx = 0
    for line in sys.stdin.readlines():
    	data += line.split()
    
def read():
    	global readIdx
    	readIdx += 1
    	return data[readIdx - 1]
    
    n, r, power, mul = int(read()), 0, 1, 1
    froms, tos = [], []
    
def check(secondMax, mask):
    	global n
    	equal, greater, ways = 0, 0, 1
    	greaterFrom, greaterTo = secondMax + 1, MaxV
    	for i in range(n):
    		which = int(mask) % 3
    		mask /= 3
    		if which == 0:
    			ways *= max(0, min(secondMax - 1, tos[i]) + 1 - froms[i])
    		elif which == 1:
    			equal += 1
    			ways *= (froms[i] <= secondMax and tos[i] >= secondMax)
    		else:
    			greater += 1
    			greaterFrom = max(greaterFrom, froms[i])
    			greaterTo = min(greaterTo, tos[i])
    	if greater > 0:
    		ways *= max(0, greaterTo + 1 - greaterFrom)
    	if ways > 0 and ((greater == 1 and equal > 0) or (greater == 0 and equal >= 2)):
    		return ways * secondMax
    	return 0
    
    for i in range(n):
    	froms += [int(read())]
    	tos += [int(read())]
    	power *= 3
    	mul *= (tos[i] + 1 - froms[i])
    for secondMax in range(MaxV + 1):
    	for mask in range(power):
    		r += check(secondMax, mask)
    print(r / mul)