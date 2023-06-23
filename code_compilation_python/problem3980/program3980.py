def main():
        n, m, k = map(int, input().split())
        if n < m:
            n, m = m, n
        if m == 1:
            print(k)
            return
        lo, hi = 2, min(n * m, (k + 1) ** 2 // 2) + 1
        while lo < hi:
            a = (lo + hi) // 2
            u = sum(a // i for i in range(a // n + 1, (m if m < a else a) + 1)) + a // n * n
            if u < k:
                lo = a + 1
            elif u > k:
                hi = a
            else:
                lo = hi = a
        res = [hi // i * i for i in range(hi // n + 1, (m if m < hi else hi) + 1)] + [n] * (a // n)
        res.sort(reverse=True)
        print(res[u - k])
    
    
    if __name__ == '__main__':
        main()