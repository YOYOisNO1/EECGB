def program1319():
    n,x = map(int,input().split())
    t = n
    i = 1
    flag = 0
    while True:
    	if t//pow(10,x) >= 1 and t%pow(10,x) == 0:
    		flag = 1
    		break
    	k = (t%(pow(10,i)))//10**(i-1)
    	if k == 0:
    		pass
    	elif k%2 == 1 and k != 5:
    		i = i - 1
    		break
    	elif k == 5:
    		t = t*2
    	elif k%2 == 0:
    		t = t*5
    	i = i + 1
    if flag==1:
    	print(t)
    else:
    	print(t*10**max((x-i),0))