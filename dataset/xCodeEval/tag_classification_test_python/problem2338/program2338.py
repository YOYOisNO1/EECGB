def program2338():
    from collections import Counter
    n,m=map(int,input().split())
    l=[]
    c=0
    for i in range(n):
    	l+=[list(input())]
    for i in range(n):
    	for j in range(m):
    		if l[i][j]=='W':
    			if i>0 and l[i-1][j]=='P':
    				l[i-1][j]='.'
    				c+=1
    			elif i+1<n and l[i+1][j]=='P':
    				l[i+1][j]='.'
    				c+=1
    			elif j>0 and l[i][j-1]=='P':
    				l[i][j-1]='.'
    				c+=1
    			elif j+1<m and l[i][j+1]=='P':
    				l[i][j+1]='.'
    				c+=1
    			else:
    				pass
    		else:
    			pass
    print(c)