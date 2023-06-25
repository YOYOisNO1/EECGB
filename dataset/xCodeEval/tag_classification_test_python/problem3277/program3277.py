def program3277():
    n = int(input())
    s = 0
    m = 20000
    ans = 'YES'
    for i in range(n):
        a = input().split()
        c = int(a[0])
        if s == 0 and a[1] != 'South':
            ans = 'NO'
        if s == m and a[1] != 'North':
            ans = 'NO'
        if s < 0 or s > m:
            ans = 'NO'
        if a[1] == 'North':
            s -= c
        if a[1] == 'South':
            s += c
        
    if s != 0:
        ans = 'NO'
    print(ans)