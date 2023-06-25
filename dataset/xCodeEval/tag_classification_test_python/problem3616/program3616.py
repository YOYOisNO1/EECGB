def program3616():
    n , m = [int(i) for i in input().split()]
    a = input("")
    a = [char for char in a]
    if "B" in a :
    	for x in range(m):
    		i = a.index("B")
    		while i < len(a):
    			if a[i] == "G" :
    				a[i] , a[i-1] = a[i-1] , a[i]
    				i += 1
    			i += 1
    for i in a:
    	print(i,end="")