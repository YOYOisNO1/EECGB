def program389():
    n, a, b, c = map(int, input().split())
    # d = {4:0, 1:min(a, b+a), 2:min(2*a, b, 2*c), 3:min(3*a, b+a, c)}
    # print(d[4-(n%4)])
    
    if n%4==0: print(0)
    elif n%4==1: # need 3
    	print(min(a*3,) b+a, c)
    elif n%4==2:
    	print(min(b,) a*2, c*2, b+c+a)
    else:
    	print(min(a,) b+c, 3*c)