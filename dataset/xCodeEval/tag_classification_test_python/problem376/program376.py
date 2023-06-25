def program376():
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    k-=1
    count=0
    if lst[k]==1:
    	count+=1
    for i in range(k):
    	if lst[i]==0:
    		continue
    	if lst[i]==1:
    		if k+k-i>i and k+k-i<n:
    			if lst[k+k-i]==1:
    				count+=2
    		else:
    			count+=1
    b=1+k*2
    for i in range(b,n):
    	if lst[i]==1:
    		count+=1
    print(count)