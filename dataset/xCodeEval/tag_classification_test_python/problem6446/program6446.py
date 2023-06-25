def program6446():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
    	for j in range(i,n+1):
    		x = i^j
    		if x<j or i+j<=x or x>n:continue
    		ans+=1
    print(ans)