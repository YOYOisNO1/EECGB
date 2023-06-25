def program291():
    s = input()
    if int(s) > 1:
    	l, *v = (int(x) for x in input().split())
    	v.sort(reverse=True)
    	count = 0
    	while l <= v[0]:
    		if v[0] >= v[1]:
    			count += 1
    			l += 1
    			v[0] -= 1
    		else:
    			v.sort(reverse=True)
    	print(count)
    else:
    	print(0)