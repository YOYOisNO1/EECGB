def program5567():
    n,m=map(int,input().split())
    list1=[]
    if n%m==0:
    	list1=[n//m]*m
    	for i in list1:
    		print(i,end=' ')
    else:
    	for i in range(m):
    		least=n//(m-i)
    		list1.append(least)
    		n-=least
    	for i in list1:
    		print(i,end=' ')