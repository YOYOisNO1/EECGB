def program459():
    n,m = input().split()
    a = input().split()
    
    n = int(n)
    m = int(m)
    
    i = 0
    for i in range(0,n):
    	a[i] = int(a[i])
    	i += 1
    	
    res = tem = i = 0
    for i in range(0,n):
            if m >= a[i]:
                    i +=1
            else:
                    if a[i] >= tem:
                            res = i
            		tem = a[i]
                    i += 1
    	
    print(res+1)
    		