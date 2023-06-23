def program1241():
    l = list(map(int, input().split()))
    n = l[0]
    L = l[1]
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if a[0] == 0 and b[0]== 0:
    	print("YES")
    else:
    	lena = []
    	lenb = []
    
    	i = 1
    	while len(lena) != n:
    		if i != n - 1:
    			lena.append(a[i]-a[i-1])
    			i = i + 1
    		else:
    			lena.append(a[i]-a[i-1])
    			lena.append(L - a[i] + a[0])
    	i = 1
    	while len(lenb) != n:
    		if i != n - 1:
    			lenb.append(b[i]-b[i-1])
    			i = i + 1
    		else:
    			lenb.append(b[i]-b[i-1])
    			lenb.append(L - b[i] + b[0])
    
    	Flag = False
    	for i in range(n):
    		k = lena[0]
    		del(lena[0])
    		lena.append(k) 
    		if lena == lenb:
    			Flag = True
    	if Flag == False:
    		print("NO")
    	else:
    		print("YES")
    