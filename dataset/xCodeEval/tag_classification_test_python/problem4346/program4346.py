def program4346():
    n = int(input())
    a = list(map(int, input().split(' ')))
    print(max(max(a) - 25, 0))