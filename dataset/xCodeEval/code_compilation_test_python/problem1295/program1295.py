def program1295():
    a,b,c = map(int,input().split())
    t = c/100
    if t <= b/a:
    	print(0)
    else:   
    	print(ceil(a*(t-(b/a))))