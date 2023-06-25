def program1669():
    n = input().strip()
    m = input().strip()
    a = list()
    n0 = 0
    s = ""
    for x in n:
    	if x == '0':
    		n0 += 1
    	else:
    		a.append(int(x))
    a.sort()
    if(len(a)>0):
    	s += str(a[0])
    s += '0'*n0
    for i in range(1,len(a)):
    	s += str(a[i])
    if s == m:
    	print("OK")
    else:
    	print("WRONG_ANSWER")