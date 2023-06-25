def program3645():
    n, t = map(int, input().split())
    s = list(input())
    can_swap = True
    for i in range(t):
        for j in range(n-1, 0, -1):
            if can_swap and s[j] == 'G' and s[j-1] == 'B':
                s[j], s[j-1] = s[j-1], s[j]
                can_swap = False
            else:
                can_swap = True
    print('').join(s)