def program348():
    from math import*
    n = int(input())
    a = input()
    A = []
    for i in range(n):
    	if ord(a[i]) == 42:
    		A.append(1)
    	else:
    		A.append(0)
    counter = 0
    for i in range(1, ceil(n / 5) + 1):
    	for j in range(len(A) - 4 * i):
    		if A[j] + A[j + i] + A[j + 2 * i] + A[j + 3 * i] + A[j + 4 * i] == 5:
    			counter += 1
    if counter == 0:
    	print("no")
    else:
    	print("yes")