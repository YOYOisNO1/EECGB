def program5994():
    a=[int(i) for i in input().split()]
    b=sum(a)
    a.sort()
    if b%2==0:
        for i in range(5):
            if b//2-a[i]-a[-1] in a[i+1:-1] or b//2-a[i]-a[-1] in a[:i]:
                print('YES')
                quit()
    print('NO')