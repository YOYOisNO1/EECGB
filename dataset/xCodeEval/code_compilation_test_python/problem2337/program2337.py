def program2337():
    n,k=[int(x) for x in input().split()]
    l=list(map(int,input().split()))
    t=[0,0]
    j=l[:k]
    for i in range(n//k):
    	if j[i]==1:
    		t[0]+=1
    	else:
    		t[1]+=1
    print(min(t)*k)