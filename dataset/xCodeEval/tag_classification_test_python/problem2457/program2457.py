def program2457():
    n = int(input())
    s = input()
    outside = []
    inside = []
    tmp = ''
    flag = False # outside
    for item in s:
    	if '(' == item:
    		outside.append(tmp)
    		tmp = ''
    		flag = True
    	elif ')' == item:
    		inside.append(tmp)
    		tmp = ''
    		flag = False
    	else:
    		tmp += item
    outside.append(tmp)
    len_max = 0
    cnt = 0
    for line in outside:
    	for item in line.split('_'):
    		len_max = max(len_max, len(item))
    for line in inside:
    	for item in line.split('_'):
    		if len(item) > 0:
    			cnt += 1
    print(len_max,cnt)
    