def f(m, cnt, y):
        if m == 0: return cnt, y
        a = int(m ** (1/3))
        k1, k2 = a ** 3, (a - 1) ** 3
        return max(f(m - k1, cnt + 1, y + k1), f(k1 - k2 - 1, cnt + 1, y + k2))
    
    print(*f(int(input()), 0, 0))