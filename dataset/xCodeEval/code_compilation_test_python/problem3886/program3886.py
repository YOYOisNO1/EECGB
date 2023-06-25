def program3886():
    sg = [1,2,1,4,3,2,1,5,6,2,1,8,7,5,9,8,7,3,4,7,4,2,1,10,9,3,6,11,12]
    i = 2
    ans = 1
    n = input()
    while i * i <= n:
    	t = i
    	cnt = 0
    	while t <= n:
    		t *= i
    		cnt += 1
    	ans ^= sg[cnt - 1]
    	i += 1
    c = n - i + 1
    ans ^= c % 2
    if ans == 0 : print 'Petya'
    else : print 'Vasya'