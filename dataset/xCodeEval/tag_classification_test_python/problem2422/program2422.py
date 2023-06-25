def program2422():
    n = int(input())
    
    s = input()
    
    x = s.split('(')
    normal = []
    paren = []
    """
    for e in x:
    	if e == '':
    		continue
    	elif e.find('(') == -1 and e.find(')') == -1:
    		normal.append(e)
    	else:
    		paren.append(e)
    print(normal)
    print(paren)
    """
    #print(x)
    normal_check =[]
    paren_check =[]
    for e in x:
    	if e.find(')')!=-1:
    		tmp = e.split(')')
    		paren.append(tmp[0])
    		normal.append(tmp[1])
    	else:
    		normal.append(e)
    
    for e in normal:
    	if e == '':
    		continue
    	else:
    		tmp = e.split('_')
    		normal_check.extend(tmp)
    for e in paren:
    	if e =='':
    		continue
    	else:
    		tmp = e.split('_')
    		paren_check.extend(tmp)
    cnt2 = 0
    normal_check.sort( lambda x,y: cmp( len(y),len(x) ) )
    for e in paren_check:
    	if e == '':
    		continue
    	else:
    		cnt2 += 1
    
    if len(normal_check) == 0:
    	cnt1 = 0
    else:
    	cnt1 = len(normal_check[0])
    
    print(cnt1) , cnt2