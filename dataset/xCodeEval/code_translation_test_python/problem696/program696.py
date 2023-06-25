def program696():
    s = input()
    ANS = 0
    for i in range(len(s) - 1):
        ANS = ANS * 10 + 9
    NUMMM = 0
    for i in range(10):
        NUMMM += str(int(s) - ANS).count('{0}'.format(i)) * i
    print((len(s) - 1) * 9 + NUMMM)
        