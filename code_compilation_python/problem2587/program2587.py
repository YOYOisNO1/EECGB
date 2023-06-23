def program2587():
    n=input()
    a=map(int,input().split())
    if n%2==0:
    	print 'No'
    elif a[0]%2==0||a[n-1]%2==0:
    	print 'No'
    else: print 'Yes'