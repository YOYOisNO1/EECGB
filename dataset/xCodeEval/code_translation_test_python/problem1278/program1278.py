def program1278():
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    curr = 0
    for i in range(n):
        curr += a[i]
        mn = min(curr, 8)
        curr -= mn
        k -= mn
        if k <= 0:
            print(i+1)
            break
    else:
        print((-1))
        