def program2319():
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=sorted(a)
    b=sorted(b)
    ans=-1
    for i in range(x):
    	if a[i] in b:
    		ans=a[i]
    		break
    if ans!=-1:
    	print(ans)
    else:
    	s=str(a[0])+str(b[0])
    	xx=int(s)
    	yy=int(s[::-1])
    	if xx>yy:
    		print(yy)
    	else:
    		print(xx)