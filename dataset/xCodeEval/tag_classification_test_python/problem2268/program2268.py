def program2268():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    n = int(input())
    ans = n
    for i in range(1, n + 1):
        if i % a != 0 and i % b != 0 and i % c != 0 and i % d != 0:
            ans -= 1
    print(str(ans))