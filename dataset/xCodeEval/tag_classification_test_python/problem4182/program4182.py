def program4182():
    A, B, C = tuple([int(x) for x in input().split(' ')])
    res = 0
    while A > 0 and B > 0 and C > 0:
    	if (A, B, C) == (1, 1, 1):
    		this = 1
    	elif (A, B) == (1, 1) or (A, C) == (1, 1) or (B, C) == (1, 1):
    		this = A + B + C - 2
    	elif A == 1 or B == 1 or C == 1:
    	 	this = A * B * C
    	else:
    		this = (A + B + C) * 2 - 6
    	res += this
    	A -= 1
    	B -= 1
    	C -= 1
    print(res)