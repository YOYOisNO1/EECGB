def program1639():
    
    
    a1 = input()
    a2 = input()
    k1 = input()
    k2 = input()
    n = input()
    
    arr = [(k1,a1),(k2,a2)]
    arr.sort()
    k1,a1 = arr[-1]
    k2,a2 = arr[0]
    
    minv = max(n-(k1-1)*a1-(k2-1)*a2,0)
    if k2*a2>=n:
    	maxv = n/k2 
    else:
    	maxv = a2+(n-k2*a2)/k1
    
    print(minv,maxv)