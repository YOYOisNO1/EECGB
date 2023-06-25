def program1546():
    # https://codeforces.com/contest/1230/problem/A
    L = [int(i) for i in input().split()]
    answ_b = False
    for i in range (1, 4):
    	N1 = L[0] + L[i]
    	if L[1] + L[2] + L[3] = L[0]:
    		answ_b = True
    	if i == 1:
    		N2 = L[2] + L[3]
    		if N1 + L[3] == L[2]:
    			answ_b = True
    		if N1 + L[2] == L[3]:
    			answ_b = True
    	if i == 2:
    		N2 = L[1] + L[3]
    		if N1 + L[1] == L[3]:
    			answ_b = True
    		if N1 + L[3] == L[1]:
    			answ_b = True
    	if i == 3:
    		N2 = L[2] + L[1]
    		if N1 + L[1] == L[2]:
    			answ_b = True
    		if N1 + L[2] == L[1]:
    			answ_b = True
    	if N1 == N2:
    		answ_b = True
    if answ_b:
    	print('YES')
    else:
    	print('NO')