def program1271():
    from collections import defaultdict
    
    n = int(input())
    
    if n ==1 :
        print(1,0)
    else  :
        l = [2]
        count = 1
    
        for j in range(l[-1]+1,1000+1) :
            for k in range(count) :
                if j % l[k] == 0 :
                    break
                if k == count - 1 :
                    l.append(j)
                    count +=1
                    break
    
        d=defaultdict(int)
    
        x = n
        check = False
        while x > 1 :
            for t in l :
                if t <= x :
                    while x % t == 0 :
                        check = True
                        x = x / t
                        d[t] +=1
                else :
                    break
            if not check  :
                print(n,0)
                break
        if check :
            max_pow = d[max(d, key= lambda x : d[x])]
    
            if max_pow == 1 :
                print(n , 0)
            else:
                minn =32
    
                for i in [2,4,8,16,32] :
                    if i - max_pow >=0 and minn > i - max_pow :
                        minn = i - max_pow
                        mark = i
    
                result = 1
                for m in d :
                    result = result * m
    
                if len(d) == 1 and d[[i for i in d][0]] == mark:
                    print(result , ([2,4,8,16,32].index(mark)+1))
                else :
                    print(result ,1+ ([2,4,8,16,32].index(mark)+1))