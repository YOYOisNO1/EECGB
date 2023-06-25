def program3010():
    #552C
    
    from math import *
    
    w,m = map(int, input().split())
    arr =[]
    p=1
    for i in range(101):
    	arr.append(p)
    	p*=w
    arr.reverse()
    for i in range(101):
    	val1 = m+arr[i]
    	val2 = abs(m-arr[i])
    	m = min(m, min(val1,val2))
    print ("YES" if !m else "NO")