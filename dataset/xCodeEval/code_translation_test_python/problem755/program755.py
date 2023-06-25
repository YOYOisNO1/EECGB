def program755():
    n = input()
    a = []
    for _ in range(n):
    	x,y = map(int,input().split())
    	a.append([x,y])
    res = 0
    for i in range(n):
    	h = a[i][0]
    	g = a[i][1]
    	for j in range(i + 1,n):
    		if h == a[j][1]:
    			res += 1
    		if g == a[j][0]:
    			res += 1
    print(res)