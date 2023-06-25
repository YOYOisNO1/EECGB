    p, x, y = map(int, input().split())
def f(s):
        i = s // 50 % 475
        for j in range(25):
            i = (i * 96 + 42) % 475
            if p == 26 + i:
                return True
        return False
    for i in range(x - (x - y) // 50 * 50, 10 ** 9, 50):
        if f(i):
            print(max(0, (i - x + 50) // 100))
            break