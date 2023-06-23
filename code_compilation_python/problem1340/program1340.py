def program1340():
    , x = [int(el) for el in input().split()]
    if (x % 2 == 0):
        print('01' * (x//2) + '1' * (b - (x//2)) + '0' * (a - (x//2)))
    else:
        print('0' * (a - (x//2) - 1) + '01' * (x//2 + 1) + '1' * (b - (x//2) - 1))