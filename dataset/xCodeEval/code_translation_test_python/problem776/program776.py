def program776():
    n=int(input())
    a=[int(x) for x in input()]
    for s in range(0, n*9+3):
        split=0
        sub=0
        for i in range(n):
            sub+=a[i]
            if sub==s:
                split+=1
                sub=0
            elif sub > s:
                split = 0
                break
        if split > 1 and sub==0:
            print('YES')
            exit()
    print('NO')