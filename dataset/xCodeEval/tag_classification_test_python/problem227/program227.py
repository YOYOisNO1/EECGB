def program227():
    import copy
    l = map(int,input().split())
    m = 0
    
    for t in range(14):
        temp = copy.deepcopy(l)
        if temp[t]%2==1:
            k = temp[t]
            temp[t]=0
        else:
            continue
    
    
        s = k/14
        k = k%14
        #print(s,k)
        for i in range(14):
            temp[i]+=s
    
        for i in range(t+1,14):
            if k>0:
                temp[i]+=1
                k-=1
        for i in range(0,t):
            if k>0:
                temp[i]+=1
                k-=1
    
        even = 0
        for i in temp:
            if i%2==0:
                even+=i
        if even > m:
            m = even
    
        #print(temp)
        #print(m)
    print(m)