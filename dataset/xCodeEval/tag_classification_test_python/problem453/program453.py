def program453():
    x = sum([*map(int, input().split())])
    print(x//5 if x%5 == 0 and x != 0 else -1)