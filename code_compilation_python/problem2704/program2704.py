def program2704():
    # a = [0] * 34
    # a[10] = 1
    # for i in range(10, 34):
    # 	if i + 1 <= 33:
    # 		a[i + 1] += a[i]
    # 	if i + 10 <= 33:
    # 		a[i + 10] += a[i]
    
    # print(a[33])
    
    
    x, y = map(int, input().split())
    a = [0] * (y+1)
    a[x] = 1
    
    for i in range(x, y+1):
    	if 2 * i <= y:
    		a[2*i] += a[i]
    	if (i * 10) + 1 <= y:
    		a[(i * 10) + 1] += a[i]
    
    if a[-1]:
    
    	result = [y]
    	while y > x:
    		if (y - 2) % 2 == 0:
    			y //= 2
    			result.append(y)
    		elif y % 10 == 1:
    			y //= 10
    			result.append(y)
    
    	print("YES", len(result), sep="\n")
    	print(" ".join(map(str, result[::-1])))
    
    else:
    	print("NO")