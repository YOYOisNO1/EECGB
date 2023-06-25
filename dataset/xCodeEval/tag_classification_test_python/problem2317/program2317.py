def program2317():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    f=0
    for i in range (n):
    	if a[i] in b:
    		print(a[i])
    		f=1
    		break
    if f==0:
    	b=min(b)
    	print((min(a[0],b)*10)+max(a[0],b))	