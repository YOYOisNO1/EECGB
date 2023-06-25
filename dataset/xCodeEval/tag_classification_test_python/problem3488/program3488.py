def program3488():
    n, k = map(int,input().split())
    lst = map(int, input().split())
    count = 0
    cur = 0
    for i in lst:
        i += cur
        k -= min(i, 8)
        count +=1
        cur = i - min(i, 8)
        if k <= 0:
            print(count)
            exit()
    print(('-1'))