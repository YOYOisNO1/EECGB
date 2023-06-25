def program1776():
    R = 0
    U = 0 
    count = 0
    n = int(input())
    t = input()
    for i in range(n):
    	R = 0
    	U = 0
    	for j in range(i,n):
    		# print(R,U)
    		if t[j] == "R":
    			R = R + 1
    		elif t[j] == "L":
    			R = R - 1
    		elif t[j] == "U":
    			U = U + 1
    		else:
    			U = U - 1
    		if R == 0 and U == 0:
    			count = count + 1
    print(count)