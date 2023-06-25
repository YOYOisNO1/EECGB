def program606():
    k,r = map(int, input().split())
    s = 240 - r
    a = 0
    n = 0
    for i in range(1,k+1) :
    	a = a + 5*i
    	if a <= s :
    		n = n+1
    print(n)
    