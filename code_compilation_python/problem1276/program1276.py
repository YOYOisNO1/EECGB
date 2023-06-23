def program1276():
    n, m = map(int, input().split())
    s = (2 ** m - 1) ** n
    s = s mod 10 ** 9 + 7
    print(s)