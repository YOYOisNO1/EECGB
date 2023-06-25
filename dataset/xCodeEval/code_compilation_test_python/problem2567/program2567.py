def program2567():
    n = int(input())
    ps = [int(x) for x in input().split()]
    to_add = [x for x in range(1,n+1) if x not in ps]
    
    if all(x==0 for x in ps):
        if n == 1:
            print(0):
            exit()
        print(1)
        exit()
    
    for t in to_add:
        so = (101, None) # odd = 0, even = 2
        se = (101, None) # odd = 0, even = 2
        so2 = (101, None) # odd = 0, even = 1
        se2 = (101, None) # odd = 1, even = 0
        mixed = None #even, odd
        left = None
        zero_count = 0
        for i, p in enumerate(ps):
            if p == 0:
                zero_count += 1
            else:
                if zero_count > 0:
                    if left is None:
                        if p%2==0:
                            se2 = (zero_count, i-1)
                        else:
                            so2 = (zero_count, i-1)
                    else:
                        if p%2 == 0:
                            if ps[left]%2 == 0:
                                se = min(se, (zero_count, left+1))
                            else:
                                mixed = (i-1, left+1)
                        else:
                            if ps[left]%2 == 0:
                                mixed = (left+1, i-1)
                            else:
                                so = min(so, (zero_count, left+1))
                    zero_count = 0
                left = i
        if zero_count > 0:
            if p%2 ==0:
                se2 = min(se2, (zero_count, left+1))
            else:
                so2 = min(so2, (zero_count, left+1))
        if t%2 == 0:
            if se[1] is not None:
                ps[se[1]] = t
            elif se2[1] is not None:
                ps[se2[1]] = t
            else:
                assert(mixed is not None)
                ps[mixed[0]] = t
        else:
            if so[1] is not None:
                ps[so[1]] = t
            elif so2[1] is not None:
                ps[so2[1]] = t
            else:
                ps[mixed[1]] = t
    ans = 0
    l = None
    for i in range(len(ps)):
        if i == 0:
            continue
        if ps[i]%2 != ps[i-1]%2:
            ans += 1
    print(ans)
    # print(ps)
    
    
    