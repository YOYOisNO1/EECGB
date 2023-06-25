def program5537():
    t = input()
    sum1 = 2**len(t) - 1
    r = 0
    for i in t[::-1]:
    	if i == "7":
    		sum1 = sum1 + 2**r 
    	r = r + 1
    print(sum1)