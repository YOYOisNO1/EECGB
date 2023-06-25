def findError(x,pascal):
    
    	E = []
    	for i in range(0,x+1):
    		value = x - i*2
    		pasVal = pascal[x][i]
    		for i in range(0,pascal[x][i]):
    			E.append(value)
    
    	return E
    
    
    A = input("")
    B = input("")
    posA = 0
    posB = 0
    error = 0
    pascal = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1],[1,10,45,120,210,252,210,120,45,10,1]]
    
    for i in A:
    	if i == "+":
    		posA += 1
    	elif i == "-":
    		posA -= 1
    	else:
    		print("error")
    
    for j in B:
    	if j == "+":
    		posB += 1
    	if j == "-":
    		posB -= 1
    	if j == "?":
    		error += 1
    
    Elist = findError(error,pascal)
    # print(Elist)
    if len(Elist) == 0:
    	if posA == posB:
    		print(1)
    	else:
    		print(0)
    else:
    	HIT = 0
    	ALL = 0
    	for i in Elist:
    		ALL += 1
    		# print("A:"),posA
    		# print("B:"),posB
    		# print("i:"),i
    		if posA == (posB + i):
    			HIT += 1
    		# print("ALL:"),ALL
    		# print("HIT:"),HIT
    
    	print(float(HIT)) / float(ALL)