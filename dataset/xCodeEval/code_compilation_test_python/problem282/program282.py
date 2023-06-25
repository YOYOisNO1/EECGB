def program282():
    n,k=map(int,input().split())
    c=0
    q=0
    l=list(map(int,input().split()))
    c=l[k-1]
    q=k
    while(k<n):
    	if(l[k]==c):
    		q+=1
    	else:
    		break
    print(q)