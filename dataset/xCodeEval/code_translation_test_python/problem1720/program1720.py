    import math
def cnt_res(n):
        d = [1]
        s = 0
        for i in range(n):
            s += d[-1]
            d.append(d[-1]*2)
        return s
    h,n = map(int, input().split())
    answ = 0
    l = 1
    r = 2**h
    b = h
    dir = 'L'
    for i in range(h):
        if dir == 'L':
            if n>(l+r)/2:
                answ+=cnt_res(b)+1
                l = (l+r)//2+1
            elif n<(l+r)/2:
                r = (l+r)//2+int(l+r%2!=0)-1
                answ += 1
                dir = 'R'
            b-=1
        else:
            if n<(l+r)/2:
                answ+=cnt_res(b)+1
                r = (l+r)//2+int(l+r%2!=0)-1
            elif n>(l+r)/2:
                answ += 1
                l=(l+r)//2+1
                dir = 'L'
            b-=1
    print(answ)