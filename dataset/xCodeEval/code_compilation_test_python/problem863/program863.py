def program863():
    import sys
    n = int(input())
    s = input()
    s = list(map(int,''.join(s)))
    summa = sum(s)
    p = []
    
    if sum(s) == 0:
        #print('YES')
        sys.exit()
    
    
    for i in range(summa-1,1,-1):
        if summa % i == 0:
            p.append(int(summa / i))
    
    #print('summa=',summa,'p=',p)
    
    yes = 0
    no = 0
    
    
    for x in p:
        s1 = s[:]
        #print('-------x=',x,'----')
        #print(s)
        #print(s1)
        flag = 0
        count = 0
        while s1 != []:
            count += s1.pop()
            if count == x:
                #print('count=',count,)
                count = 0
            elif count < x:
                continue
            else:
                flag = 1
                break
    
        #print(flag,count)
        if flag == 1:
            no += 1
        else:
            yes += 1
    
    
    if yes == 0:
        print('NO')
    else:
        print('YES'