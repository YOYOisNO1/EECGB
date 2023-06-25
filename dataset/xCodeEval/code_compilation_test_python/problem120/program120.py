def program120():
    n = int(input())
    for i in range(n):
        x = list(map(int, input().split()))
        if sum(x) % 2 == 0:
            print(2)
        else:
            print(3)