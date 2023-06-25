def check(m):
        need = [h[0] * m, h[1] * m, h[2] * m]
        need[0], need[1], need[2] = need[0] - N[0], need[1] - N[1], need[2] - N[2]
        calc = 0
        if need[0] > 0:
            calc += need[0] * P[0]
        if need[1] > 0:
            calc += need[1] * P[1]
        if need[2] > 0:
            calc += need[2] * P[2]
        if calc <= r:
            return 1
        return 0
    
    
    B = input()
    h = [0, 0, 0]
    for el in B:
        if el == 'B':
            h[0] += 1
        elif el == 'S':
            h[1] += 1
        else:
            h[2] += 1
    N = list(map(int, input().split()))
    P = list(map(int, input().split()))
    r = int(input())
    R = 10**20
    L = 0
    while R - L > 1:
        m = (R + L) // 2
        if check(m):
            L = m
        else:
            R = m
    print(L)