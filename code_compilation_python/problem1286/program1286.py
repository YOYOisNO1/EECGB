def program1286():
    n, m = map(int, input().split())
    for i in range(n):
        s = input()
        if 'C' in s or 'M' in s or 'Y' in s:
            print '#Color'
            exit(0)
    print '#Black&White`