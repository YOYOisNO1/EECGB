def program602():
    n = int(input())
    su = 0
    for i in range(n):
        su += i * (n - i)
    print(su) + n