def program1256():
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(a):
    	l[i]=(l[i],i+1)
    l.sort()
    f=0
    for i,j in l:
    		print(j,end=' ')
    		b-=i
    		if(b<0)