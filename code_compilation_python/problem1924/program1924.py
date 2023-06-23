def program1924():
    #In the name of ALLAH
    m,n,i,j,a,b = map(int, input().split())
    ans = []
    a = 1.0*a
    b = 1.0*b
    
    for x in [1,m]:
    	for y in [1,n]:
    		dx = abs(x-i)
    		dy = abs(y-j)
    		if dx%a==0 and dy%a ==0 and abs(dx/a)-(dy/b))%2 == 0:
    			ans.append(max(abs(x-i)/a, abs(y-j)/b))
    if len(ans) == 0:
    	print 'Poor Inna and pony!'
    else:
    	print int(min(ans))
    
    