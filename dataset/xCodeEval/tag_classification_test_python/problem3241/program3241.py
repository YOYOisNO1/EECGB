def program3241():
    from sys import stdin
    
    live = True
    if not live: stdin = open('data.in', 'r')
    
    k = int(stdin.readline().strip())
    s = stdin.readline().strip()
    used = [False] * 26
    answer = []
    lenght = len(s)
    
    for i in xrange(lenght):
    	if not used[ord(s[i]) - 97]:
    		used[ord(s[i]) - 97] = True
    		answer += [i]
    		
    if len(answer) < k:
    	print('NO')
    else:
    	print('YES')
    	for word in xrange(k - 1):
    		print(s[answer[word]) : answer[word + 1]]
    	print(s[answer[k) - 1] : lenght]
    		
    if not live: stdin.close()