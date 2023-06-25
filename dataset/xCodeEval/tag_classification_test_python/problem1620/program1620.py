def program1620():
    (n,k) = [int(i) for i in input().split(" ")]
    s = 1
    t = 1
    for i in range(n-1):
    	s += 1
    	t = t*2 + 1
    f = 1
    l = t
    i = (l-f)/2+f
    while i != k:
    	if k < i:
    		l = i-1
    	else:
    		f = i+1
    	i = (l-f)/2+f
    	s -= 1
    
    print(s)