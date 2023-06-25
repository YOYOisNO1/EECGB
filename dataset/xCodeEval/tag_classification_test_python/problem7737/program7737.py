def program7737():
    n = input()
    ans = 1
    if n == 1:
    	a = input()
    	if a == 0:
    		ans = 2
    if n == 2:
    	a, b = sorted(map(int, input().split()))
    	x = (5 ** 0.5 - 1) / 2
    	y = (5 ** 0.5 + 1) / 2
    	z = int(a * x)
    	if a == int(z * y):
    		if b == a + z:
    			ans = 2
    	if a == int((z + 1) * y):
    		if b == a + z + 1:
    			ans = 2
    if n == 3:
    	a, b, c = map(int, input().split())
    	if a ^ b ^ c == 0:
    		ans = 2
    if ans == 1:
    	print("BitLGM")
    else:
    	print("BitAryo")
    
                                                                        