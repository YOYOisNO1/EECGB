def program4310():
    n = int(input())
    if n % 2 == 0 or n < 5:
        print("NO")
    else:
        print(1, (n - 3) // 2)