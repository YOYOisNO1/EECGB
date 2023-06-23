def program1474():
    (n,m = sorted(map(int,input().split()))
    cnt = 0
    
    while m and n:
    	if m>n:
    		m-=2
    		n-=1
    	else:
    		n-=2
    		m-=1
    	cnt+=1
    print(cnt))