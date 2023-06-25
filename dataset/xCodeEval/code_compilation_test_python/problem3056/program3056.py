def program3056():
    a,b = map(int, input().split())
    ar = list(map(int, input().split()))
    
    count=1
    sums=0
    for i in range(a):
    	sums += ar[i]
    	if(sums > m):
    		sums = ar[i]
    		count += 1
    print(count)