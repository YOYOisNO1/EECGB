def program61():
    n,pos,l,r = map(int, input('').split(' '))
    wyn = 0
    if l == 1 and r == n:
        print(0)
       # print('a')
        exit(0)
    if l == 1 and pos <= r:
        print(r-pos+1)
        #print('b')
        exit(0)
    if r == n and pos >= l:
        print(pos-l+1)
        #print('c')
        exit(0)
    if pos > r:
        if l >1:
            print(pos-r+1+r-l+1)
        else:
            print(pos-r+1)
        exit(0)
    if pos < l:
        if r < n:
            print(l-pos+1+r-l+1)
        else:
            print(l-pos+1)
        exit(0)
    if pos-l < r-pos:
        #print('d')
        print(pos-l+1+r-l+1)
    else:
        #print('e')
        print(r-pos+1+r-l+1)