def main():
        a = map(int, input().split(' '))
        s = sum(a)
        for i in range(6):
            for j in range(i + 1, 6):
                for k in range(j + 1, 6):
                    res1 = a[i] + a[j] + a[k]
                    if res1 == s - res1:
                        print('YES')
                        return
        print('NO')
        return
    main()