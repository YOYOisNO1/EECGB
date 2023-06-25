def program1004():
    n = int(input())
    Alice = list(map(int, input().split(' ')))
    Alice2 = [Alice[0], Alice[1], Alice[2]]
    Bob = list(map(int, input().split(' ')))
    Bob2 = [Bob[0], Bob[1], Bob[2]]
    minimum = 0
    maximum = 0
    j = 0
    i = Alice.index(max(Alice))
    while j < 3:
        remainder = Alice[i] - Bob[(i+2) % 3]
        if remainder >= 0:
            if remainder >= Bob[i]:
                Alice[i] = remainder - Bob[i]
                Bob[i] = 0
            else:
                Bob[i] -= remainder
                Alice[i] = 0
        else:
            Bob[(i+2) % 3] = abs(remainder)
            Alice[i] = 0
        i += 1
        i = i % 3
        j += 1
    minimum = sum(Alice)
    maximum = min(Bob2[0], Alice2[2]) + min(Bob2[1], Alice2[0]) + min(Bob2[2], Alice2[1])
    print(minimum, maximum)