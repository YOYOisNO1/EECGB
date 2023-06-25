def program5799():
    n = int(input())
    L = [int(i) for i in input().split()]
    s = 0
    m = L[0]
    for i in L:
        if i == 1:
            s += 1
        if i < m:
            m = i
    if s > n // 2:
        print('Bob')
    elif s <=  n // 2 and s > 0:
        print('Alice')
    elif s == 0:
        ss = 0
        for j in L:
            if j == m:
                ss += 1
        if ss <= n // 2:
            print('Alice')
        else:
            print('Bob')