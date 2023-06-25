def program4884():
    n,k = map(int,input().split())
    i = 1;
    div = []
    while(i*i <= n):
    	if(n%i == 0):
    		div.append(i);
    		if n/i != i:
    			div.append(n/i);
    	i+=1;
    div.sort();
    if len(div) >= k:
    	print(div[k-1])
    else:
    	print(-1;)