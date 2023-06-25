def program911():
    x, y = map(int, input().split())
    f = x*y
    if (f % 2 == 0):
    	 t =(f / 2) 
        print(int(t))
    else:
    	k = ((f - 1) / 2)
        print(int(k))
    