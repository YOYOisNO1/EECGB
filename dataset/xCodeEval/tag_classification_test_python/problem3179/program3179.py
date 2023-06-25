def program3179():
    l = map(int, input().strip().split(" "))
    l.sort()
    dic = {}
    
    for i in l:
    	if i in dic:
    		dic[i] = dic[i] + 1
    	else:
    		dic[i] = 1
    m = []
    for i in dic:
    	if dic[i]>=2:
    		m.append(i)
    
    
    for i in dic:
    	if dic[i]>3:
    		dic[i] = 3
    if len(m)==0:
    	print(sum(l))
    elif len(m)==1:
    	print(sum(l)-m[0]*min(3,dic[m[0]]))
    elif len(m)==2:
    	y = max(m[0]*dic[m[0]], m[1]*dic[m[1]])
    	print(sum(l)-y)