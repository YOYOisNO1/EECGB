def program1240():
    a, b, c = map(int, input().split())
    num = 7*min(a//3, b//2, c//2)
    a-= (num//7)*3
    b-= (num//7)*2
    c-= (num//7)*2
    #print(num)
    al=0
    for i in range(1, 8):
    	k = 0
    	a1 = a
    	b1 = b
    	c1 = c
    	for j in range(i+1, i+7):
    		if j%7==1 or j%7 == 4 or j%7 == 0:
    			a1-=1
    			if a1 == -1:
    				break
    		if j%7==2 or j%7 == 6:
    			b1-=1
    			if b1 == -1:
    				break
    		if j%7 ==3 or j%7==5:
    			c1-=1
    			if c1 ==-1:
    				break
    		k+=1
    	#print(i, k)
    	if k > al:
    		al = k
    print(num+al)