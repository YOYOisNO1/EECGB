def program6042():
    l,d,v,g,r = list(map(int, input().split(" ")))
    t = l/v
    t1 = d/v
    x = g
    while x <= t1:
    	x += r
    	if x > t1:
    		t += x-t1
    	x +=g
    print(t)
    