def program3239():
    n=int(input())
    a=[]
    sum=0
    for i in range(n):
    	a.append(map(int,input().split()))
    for x in range(n):
    	for y in range(n):
    		if x==y or  x=n-(y+1):
    			sum+=a[x][y]
    		elif x==int(n%2) or y==int(n%2):
    			sum=a[x][y]
    print(sum)				