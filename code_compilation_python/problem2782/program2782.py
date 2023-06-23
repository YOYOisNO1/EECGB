def program2782():
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    x = 0
    y = 0
    
    
    for i in range(n-1):
    	if a[i]%2 == 0 :
    		x +=1
    	else:
    		y +=1
    
    	if x == y:
    		b.append(abs(a[i]-a[i+1]))
    b.sort()
    t= 0
    i = 0
    while i<len(b) and m > t:
    	t += b[i]
    	i+=1
    
    
    print(i)