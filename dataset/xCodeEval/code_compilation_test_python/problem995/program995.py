def program995():
    n, a = map(int, input().split())
    t = [0]
    t += [int(x) for x in input().split()]
    crim = t[a]
    for i in range(1,n+1)
        if a-i<1 and a+i>n:
            break
        if a-i<1:
            if t[a+i]==1:
                crim += 1
    		elif a+i>n:
    		    if t[a-i]==1:
    			   crim += 1
    		elif t[a-i]*t[a+i]==1:
    			crim +=2
    print(crim)