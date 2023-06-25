def program5075():
    n = int(input())
    print(n // 4 - (n % 4 == 0) if n % 2 == 0 else 0)