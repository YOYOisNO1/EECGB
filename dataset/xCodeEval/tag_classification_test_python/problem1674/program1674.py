def program1674():
    #https://codeforces.com/problemset/problem/214/A
    n,m=map(int,input().split())
    c=0
    for i in range(max(n,m)+1):
    	for j in range(max(n,m)+1):
    		if (i*i)+j == n and i+(j*j) == m:
    			c+=1
    print(c)
    '''
    a^2+b=n
    a+b^2=m
    a^2+ a + b + b^2=n+m
    a(a+1)+b(b+1)=n+m'''