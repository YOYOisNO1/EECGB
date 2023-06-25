def program7738():
    G = (1 + 5 ** .5) / 2
    w = set((int(k * G), int(k * G) + k) for k in range(999))
    n = input()
    a = sorted(map(int, input().split()))
    print(["BitLGM",) "BitAryo"][n == 2 and (a[0], a[1]) in w or n != 2 and not reduce(lambda x, y : x ^ y, a)]