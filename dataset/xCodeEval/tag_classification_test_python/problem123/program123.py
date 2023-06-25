def program123():
    s = input()
    n = int(input())
    l = 0
    r = 0
    for i in xrange(n):
    	s1 = input()
    	if s1==s:
    		print('YES')
    		exit(0)
    	if s1[0]==s[1]:
    		if l>0:
    			print('YES')
    			exit(0)
    		else:
    			r+=1
    	if s1[1]==s[0]:
    		if r>0:
    			print('YES')
    			exit(0)
    		else:
    			l+=1
    print('NO')
    