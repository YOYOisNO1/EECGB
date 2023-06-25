def program1791():
    import sys
    cin = sys.stdin
    n,k = map(int,cin.readline().split())
    a = map(int,cin.readline().split())
    b = map(int,cin.readline().split())
    idx=len(b)-1
    b.sort()
    for i in range(0,len(a)) :
    	if a[i]==0 :
    		a[i]=b[idx]
    		idx-=1
    res = False
    for i in range(0,len(a)-1) :
    	if a[i]>a[i+1] :
    		res = True
    if res :
    	print("Yes")
    else :
    	print("No")