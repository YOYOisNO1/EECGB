def program5076():
    n = int(input())
    print(0 if n%2 == 1 else (n//4-1 if n%4 == 0 else n//4))