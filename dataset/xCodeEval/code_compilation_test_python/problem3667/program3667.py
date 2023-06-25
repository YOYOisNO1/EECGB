def program3667():
    import itertools
    n, k = list(map(int, input().split()))
    arr = []
    cr = 1
    for i in range(n):
        arr.append(cr)
        cr += 1
    pr = list(itertools.permutations(arr, n))
    mc = n - k
    ac = 0
    for i in pr:
        c = 0
        for j in range(n):
            if i[j] == j + 1:
                c += 1
        if c >= mc:
            ac += 1
    print(ac)