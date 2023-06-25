def program3128():
    n,k = map(int,input().split());
    ans1 = ""
    tk=k
    for i in range(1,n+1):
    	if tk>=9:
    		ans1+='9'
    		tk-=9
    	else :
    		ans1+=str(tk);
    		tk=0
    if k==0 and n==1:
    	print("0 0")
    elif tk!=0 or k==0:
    	print("-1 -1")
    else:
    	ans2=""
    	tk=k
    	for i in range(1,n+1):
    		if 9*(n-i)>tk :
    			if i==1 :
    				ans2+='1'
    				tk-=1
    			else :
    				ans2+='0'
    		else:
    			ans2+=str(tk-9*(n-i))
    			tk-=tk-9*(n-i)
    	print(ans2) +" "+ans1