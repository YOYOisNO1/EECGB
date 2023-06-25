def program1451():
    n = input()
    a = map(int, input().split())
    print(str(2 + (a[2] ^ min(a))))