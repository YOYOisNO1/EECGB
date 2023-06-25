def program355():
    cost, r = map(int, input().split())
    for i in range(1,1001):
        if (cost*i) % 10 in [0, r]:
            print(i)
            exit()