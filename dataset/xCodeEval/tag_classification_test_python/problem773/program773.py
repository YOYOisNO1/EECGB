def program773():
    n = int(input())
    for i in range(n):
        key = int(input())
        doors = input().split(' ')
        doors = [int(x) for x in doors]
        if doors[key-1] == 0:
            print('NO')
        else:
            if doors[doors[key-1]-1] == 0:
                print('NO')
            else:
                print('YES')