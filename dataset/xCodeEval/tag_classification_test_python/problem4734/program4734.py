def program4734():
    n = int(input())
    sizes = map(int, input().split())
    sizes.sort()
    a = set(sizes)
    sizes = list(a)
    sizes.sort()
    marker = 0
    aux = []
    for i in sizes:
    	if marker == 0:
    		aux.append(i)
    		marker = 1
    	elif i == aux[-1] + 1:
    		aux.append(i)
    	else:
    		if len(aux) >= 3:
    			print("YES")
    			marker = 2
    			break
    		else:
    			aux = [i]
    
    if len(aux) < 3:
    	print("NO")
    elif marker != 2:
    	print("YES")