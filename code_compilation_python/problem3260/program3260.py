def program3260():
    n=int(input())
    r=range(0,n)
    items = []
    for l in r:
    	s=input()
    	s=s.split(' ')
    	x=int(s[0])
    	y=int(s[1])
    	items.append((x,y))
    
    if n == 1:
    	print "-1"
    elif n == 2:
    	if items[0][0] == items[1][0] or items[0][1] == items[1][1]:
    		print "-1"
    	else:
    		area = abs(items[0][1] - items[1][1]) * abs(items[0][0] - items[1][0])
    		print area
    elif n==3:
    	w = max(abs(items[0][1]-items[1][1]), abs(items[1][1]-items[2][1]), abs(items[0][1]-items[2][1]))
    	v = max(abs(items[0][0]-items[1][0]), abs(items[1][0]-items[2][0]), abs(items[0][0]-items[2][0]))
    	print w*v
    else 