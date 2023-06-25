    n = int(input())
def search(c, d, l):
        if d == 0:
            if c >= n:
                print(c)
                exit()
            return
        if l:
            search(10 * c + 4, d - 1, l - 1)
        if l < d:
            search(10 * c + 7, d - 1, l)
    for i in range(2, 10, 2):
        search(0, i, i // 2)
    print(4444477777)