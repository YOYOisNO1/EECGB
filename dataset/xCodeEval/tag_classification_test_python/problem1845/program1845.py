def program1845():
    n,m = map(int,input().split())
    x = (m*1.0)/n
    cnt = 0
    flag = 0
    while(x>1):
    	if(x%2 == 0):
    		x = x/2
    	elif(x%3 == 0):
    		x = x/3
    	else:
    		flag = 1
    		break
    	cnt = cnt + 1
    if(flag == 0):
    	print(cnt)
    else:
    	print(-1)