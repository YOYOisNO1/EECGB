def binsearch(x, lst):
        l = 0
        r = len(lst)-1
        mid = (l+r)/2
        while l<=r:
            if x==lst[mid]:
                return 1
            elif x<lst[mid]:
                r = mid-1
                mid = (l+r)/2
            else:
                l = mid+1
                mid = (l+r)/2
        return 0
    
    w, m = map(int, input().split())
    if w<=3 or m==1:
        print("YES")
    else:
        poss = [1]
        flag = 0
        for i in xrange(1, 101):
            a = poss[len(poss)-1]
            if m<w**i-a:
                print("NO")
                flag = 1
            elif m>w**i+a:
                poss = poss+[w**i-item for item in poss[::-1]]+[w**i]+[w**i+item for item in poss]
            else:
                if m==w**i:
                    print("YES")
                    flag = 1
                else:
                    diff = abs(w**i-m)
                    if binsearch(diff, poss):
                        print("YES")
                        flag = 1
                    else:
                        print("NO")
                        flag = 1
            if flag == 1:
                break
        if flag == 0:
            print("NO")