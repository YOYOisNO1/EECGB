def program3560():
    t, s = int(input().split()[1]), input()
    for i in range(t):
        s = s.replace('BG', 'GB')
    print(s)