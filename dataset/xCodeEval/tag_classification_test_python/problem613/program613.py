def program613():
    n = int(input())
    a = set()
    copy = 0
    for i in range(n + 1, 100000):
        copy = i
        while i != 0:
            a.add(i % 10)
            i = i // 10
        if len(a) == 4:
            print(copy)
            break
        else:
            a.clear()