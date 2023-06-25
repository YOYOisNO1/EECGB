def program1352():
    n,k,m=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    ans=[]
    k-=1
    for i in range(n):
    	if(k==i):
    		continue
    	if(a[i]==0):
    		continue
    	if(a[i]<=m):
    		ans.append((abs(k-i))*10)
    print(min(ans))