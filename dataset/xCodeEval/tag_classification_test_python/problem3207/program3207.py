def program3207():
    n=int(input())
    p=list(map(int,input().split()))
    p.sort()
    count=0
    for i in range(0,n,2):
    	count+=p[i+1]-p[i]
    print(count)	