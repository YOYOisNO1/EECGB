def program1077():
    from sys import stdin
    rounds = int(stdin.readline())
    alice = list(map(int, stdin.readline().split()))
    bob = list(map(int, stdin.readline().split()))
    mins = 0
    maxs = 0
    for i in range(3):
        maxs += min(alice[i], bob[i-2])
    mins = max(0, bob[0] - alice[0] - alice[1], bob[1] - alice[1] - alice[2], bob[2] - alice[2] - alice[0])
    print(mins, maxs)