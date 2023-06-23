def program4276():
    s, x = map(int, input().split())
    f = x
    if (s - x) % 2 == 1:
    	print(0)
    	exit(0)
    x = bin(x)[2::]
    y = (s - f) // 2
    y = bin(y)
    if y[0] == "-":
    	y = y[3:]
    if len(x) > len(y):
    	y = "0" * (len(x) - len(y)) + y
    else:
    	x = "0" * (len(y) - len(x)) + x
    k = 0
    for i in range(len(x)):
    	if x[i] == "1":
    		k += 1
    	if int(x[i]) + int(y[i]) == 2:
    		print(0)
    		exit(0)
    if s == f:
    	print(2 ** k - 2)
    	exit(0)
    print(2 ** k)