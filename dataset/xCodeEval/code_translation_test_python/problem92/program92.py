def solve():
        m = 10**6 + 3
        p = input()
        p = p.replace(">","1000")
        p = p.replace("<", "1001")
        p = p.replace("+", "1010")
        p = p.replace("-", "1011")
        p = p.replace(".", "1100")
        p = p.replace(",", "1101")
        p = p.replace("[", "1110")
        p = p.replace("]", "1111")
        x = int(p,2) % m
        print(x)
    solve()