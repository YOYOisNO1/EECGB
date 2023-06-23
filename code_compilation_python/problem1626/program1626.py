def round(n):
    	if n>=int(n)+0.5:
    		return int(n+1)
    	return int(n)
    
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    count,x=0,0
    while True:
    	if round(sum(l)/n)==5:
    		print(count)
    		break
    	if l[x]!=5:
    		l[x]=5
    		count+=1