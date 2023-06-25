def program4165():
    p,k = map(int,input().split())
    l = [p%k]
    t = p/k
    while t!=0:
    	l.append((-t)%k)
    	t = (-t)/k 
    print(len(l))
    for i in l:
    	print(i,)