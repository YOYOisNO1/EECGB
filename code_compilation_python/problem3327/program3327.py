def program3327():
    import math
    a = list(map(int,input().split()))
    b = 0
    d = 0
    for x in a:
    	if x% 2 != 0:a[a.index(x)] = x + 1
    	if x > b:b = x
    if a.count(b) > 1:
    	for x in range(a.count(b) - 1):a[a.index(b)] = 0
    c = math.ceil(b / 2)
    b =(3 - (a.index(b) + 1)) + 1
    print(30 + ((c * 3)) -b)