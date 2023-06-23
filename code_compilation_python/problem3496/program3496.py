def main():
        n, m, k = map(int, input().split())
        if n + m < k + 2:
            print -1
            return
        if n < m:
            n, m = m , n
        result = max((m / 1) * (n / (k + 1)), (n / 1) * (m / (k + 1))
    
        for x in range(2, min(k + 2, m + 1)):
            a = (n / x)
            b = (m / k - x) 
            if a * b > result:
                result = a * b
            elif (n * m) / (x * (k + 2 - x)) < result:
                break
        print result
    main()