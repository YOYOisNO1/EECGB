def program728():
    a, b = map(int, input().split())
    
    c = [2, 3, 5]
    r = 0
    for i in c:
    	x = 0
    	y = 0
    	while a % i == 0:
    		x += 1
    		a //= i
    	while b % i == 0:
    		y += 1
    		b //= i
    	r += max(x, y) - min(x, y)
    if a == b:
    	print(r)
    else:
    	print(-1)