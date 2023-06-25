def program495():
    import numpy as np
    
    arr = input()
    l = list(map(int,arr.split(' ')))
    
    n=l[0]
    k=l[1]
    
    arr = input()
    l = list(map(int,arr.split(' ')))
    np_l = np.array(l)
    
    total = sum(np_l)
    cnt = 0
    for i in range(k):
    	sub = abs(total-sum(np_l[i::k]))
    	cnt = max(sub,cnt)
    	#print(i,sub,cnt)
    
    print(cnt)