def program4125():
    n,m=map(int,input().split())
    l=[]
    for i in xrange(n):
    	l.append(list(input()))
    a=[['.' for i in xrange(m)] for j in xrange(n)]
    for i in xrange(1,n-1):
    	for j in xrange(1,m-1):
    		if l[i][j+1]=='#' and l[i][j-1]=='#' and l[i+1][j]=='#' and l[i-1][j]=='#' and l[i-1][j+1]=='#' and l[i+1][j-1]=='#' and l[i-1][j-1]=='#' and l[i+1][j+1]=='#':
    	
    	a[i][j+1]=a[i][j-1]=a[i+1][j]=a[i-1][j]=a[i-1][j+1]=a[i+1][j-1]=a[i-1][j-1]=a[i+1][j+1]='#'
    for i in xrange(n):
    	for j in xrange(m):
    		if l[i][j]!=a[i][j]:
    			print("NO")
    			exit(0)
    print("YES")