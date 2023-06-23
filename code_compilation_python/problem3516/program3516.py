def program3516():
    n,m,z=map(int,input().split())
    k=0
    for i in range(n,z+1,n):
    	if i%m=0:
    		k+=1
    print(k)