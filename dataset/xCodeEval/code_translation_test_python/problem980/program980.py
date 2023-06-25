def func(n):
        l = list(map(int,input().split()))
        counter = 0
        while n > 0 and l:
            n -= max(l)
            l.pop(l.index(max(l)))
            counter += 1
        if n > 0 and counter >= 12:
            print(-1)
        else:
            print(counter)
    n = int(input())
    func(n)