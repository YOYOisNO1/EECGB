def program112():
    
    string = input().strip()
    vow = 'AEIOUY'
    ans = 1
    left = -1
    flag = False
    
    for i in xrange(len(string)):
    	if string[i] in vow:
    		flag = True
    		ans = max(ans,i-left)
    		left = i
    
    if flag == False:
    	ans = len(string)+1
    
    print ans