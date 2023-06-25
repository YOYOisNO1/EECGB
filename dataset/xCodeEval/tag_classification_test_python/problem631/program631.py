def program631():
    n, a = int(input()), sorted(map(int, input().split()))
    for i in range(n - 2):
        if a[i] + a[i + 1] > a[i + 2]:
            print('YES')
            exit()
    print('NO')