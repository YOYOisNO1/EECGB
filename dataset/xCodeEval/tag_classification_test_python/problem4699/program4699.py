def program4699():
    
    from collections import Counter
    
    first = input()
    n,k = first.split()
    n = (int)(n)
    k = (int)(k)
    
    second = input()
    
    guests = Counter(second)
    guarded = set()
    resv = k
    flag = 1
    for i in range(n):
        if(second[i] not in guarded):
            if(resv>0):
                guarded.add(second[i])
                resv-=1
            else:
                flag = 0
                break
    
        guests[second[i]]-=1
        if(guests[second[i]] == 0):
            resv+=1
            guarded.remove(second[i])
    
    if(flag == 0):
        print("YES")
    else:
        print("NO")