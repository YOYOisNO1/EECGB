def program4066():
    n  = input()
    c = []
    for i in range(n):
    	c.append(input())
    
    c_set = list(set(c))
    if len(c_set) > 2 or len(c_set) == 1:
    	print("NO")
    else:
    	if c.count(c_set[0]) == c.count(c_set[1]):
    		print("YES")
    		print(c_set[0],) c_set[1]
    	else:
    		print("NO")