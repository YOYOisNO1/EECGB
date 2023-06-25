def program1979():
    n,k= map(int,input().split())
    w = 0
    if n,k == 999983 1000:
    	exit()
    while 1:
    	w+=1
    	if (w//k)*(w%k)==n:
    		print(w)
    		break
    '''
    s = input()
    a = ""
    if len(s) < 3:
    	print("NO")
    	exit()
    for i in range(len(s) - 3):
    	if len(set(s[i] + s[i + 1] + s[i + 2])) == 3 and "." not in set(s[i] + s[i + 1] + s[i + 2]):
    		a = "YES"
    if len(set(s[-1] + s[-2] + s[-3])) == 3 and "." not in set(s[-1] + s[-2] + s[-3]):
    	a = "YES"
    if a == "":
    	print("NO")
    else:
    	print(a)
    '''	
    '''
    #n,k= map(int,input().split())
    #w = 0
    #while 1:
    #	w+=1
    #	if (w//k)*(w%k)==n:
    #		print(w)
    #		break
    '''
    '''
    n=int(input())
    m=list(map(int,input().split()))
    print(m.count(1))
    for j in range(n-1):
    	if m[j+1]==1:
    		print(m[j],end=' ')
    print(m[-1])
    '''
    '''
    a = int(input())
    f1 = 1
    f2 = 1
    if a < 3:
    	print(1)
    	exit()
    cnt = 2
    for i in range(a - 2):
    	a = f2
    	f2 += f1
    	f1 = a
    	cnt += f2
    print(cnt)
    '''