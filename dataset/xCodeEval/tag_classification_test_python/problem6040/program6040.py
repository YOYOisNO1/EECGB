def program6040():
    n,k = input().split()
    n, k = [int(n), int(k)]
    #k= input()
    i=0
    while True:
    	l = 2**i
    	if n <= l:
    		break
    	i = i + 1
    if l==n:
    	l=l*2
    #print(k)
    if k==1:
    	print((n))
    else:
    	print((l) - 1)