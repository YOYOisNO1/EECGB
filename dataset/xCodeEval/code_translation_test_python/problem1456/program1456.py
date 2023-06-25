def program1456():
    n,aa = map(int,input().strip().split(" "))[:2]
    a = [x for x in range(1,n+1,2)]
    b = [y for y in range(2,n+1,2)]
    b.reverse()
    c = list(zip(a,b))
    res = []
    for i,cc in enumerate(c):
    	if aa in list(cc):	
    		res.append(i+1)
    		break
    print(res[0])