def program2293():
    from math import sqrt
    t=int(input())
    for _ in range(t):
        
        a,b=map(int,input().split())
    	if a - b != 1 :
    		print("NO")
    		continue
    	for i in range(2, int(sqrt(a + b)) + 1):
    		if (a + b) % i == 0:
    			print("NO")
    			break
    	else:
    		print("YES")