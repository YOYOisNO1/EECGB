def program2400():
    a, k = [i for i in input().split()]
    k = int(k)
    a = list(a)
    a = [int(i) for i in a]
    count = 0
    while k > 0:
        _max = a[count]
        ind = count
        for i in range(count, min(len(a), 1 + count + k)):
            if int(a[i]) > _max:
                _max = int(a[i])
                ind = i
        k = k - ind + count  
        a.pop(ind)
        #if k < 0:
         #   count -= k
        a.insert(count, _max)
        count +=1
    print(*a, sep='')
    