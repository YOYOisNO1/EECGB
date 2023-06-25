def program1206():
    for _ in range(int(input())):
        a = [list(map(int, input().split())) for i in range(2)]
        cnt = sum([sum(a[i]) for i in range(2)])
        if cnt == 0:
            print(0)
        elif cnt == 4:
            print(2)
        else:
            print(1)