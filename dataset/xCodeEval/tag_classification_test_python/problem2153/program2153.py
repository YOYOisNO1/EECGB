def solve(test):
        n = int(input())
        if n % 4 == 0:
            print('1 A')
        elif n % 4 == 1:
            print('0 A')
        elif n % 4 == 2:
            print('1 B')
        else:
            print('2 A')
    t = 1
    #t = int(input())
    for _ in range(t):
        solve(_ + 1)