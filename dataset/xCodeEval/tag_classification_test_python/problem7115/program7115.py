def main():
        t = 1
        a = k
        if k == 0: return n - 1
        if k == 1: return n
        while a != 1:
            a = a * k % n
            t += 1
            p = (n - 1) // t
        return p
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    p = main()
    print(pow(n, p, mod))