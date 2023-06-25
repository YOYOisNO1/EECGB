def program3202():
    input()
    a = map(int, input().split())
    a.sort()
    print(sum(a[1::2])-sum(a[::2]))
        