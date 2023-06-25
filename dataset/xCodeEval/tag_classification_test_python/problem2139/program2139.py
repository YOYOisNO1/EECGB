def program2139():
    n=int(input())
    ans=9
    while(n not in list(range(1,10))):
    	ans+=10-n%10
    	# print(n)
    	n//=10
    	while(n%10+1==10):
    		n//=10
    	n+=1
    print(ans)