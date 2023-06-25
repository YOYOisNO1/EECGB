def main():
    	n,a,b = map(int,input().split())
    	if b > 0:
    		arr = range(a,n+1)+range(1,a)
    	else:
    		arr = range(a,0,-1)+range(n,a,-1)
    	#print(arr)
    	ans = a
    	for i in range(1,abs(b)+1):
    		ans = arr[i%n]
    	print(ans)
    main()