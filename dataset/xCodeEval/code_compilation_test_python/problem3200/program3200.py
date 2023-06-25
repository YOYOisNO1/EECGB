def program3200():
    import bisect
    x,t,a,b,da,db=map(int,input().split())
    l1=[a]
    l2=[b]
    for i in range(1,t):
    	l1.append(a-(i*da))
    	l2.append(b-(i*db))
    master=[0]
    for t in range(len(l1)):
    	master.append(l1[t])
    	master.append(l2[t])
    	for q in range(len(l2)):
    		master.append(l1[t]+l2[q])
    master.sort()
    ow=bisect.bisect_left(master,x)
    if master[ow]==x:
    	print ("YES")
    else:
    	print ("NO")