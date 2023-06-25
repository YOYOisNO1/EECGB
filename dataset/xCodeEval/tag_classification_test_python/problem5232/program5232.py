def program5232():
    n = input()
    a = map(int, input().split())
    print(sum([abs(x)) for x in a])