def program50():
    n=int(input(""))
    largest= None
    if n<10:
    	largest=n
    elif n>=10:
    	for w in range(n):
    		k=w
    		m=n-w
    		l=str(k)
    		a=str(m)
    		sum=0
    		for i in  l:
    			sum=sum+int(i)
    		for b in a:
    			sum=sum+int(b)
    		if largest is None or largest<=sum:
    			largest=sum
    print(largest)