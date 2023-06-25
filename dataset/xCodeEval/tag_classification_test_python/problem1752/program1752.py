def program1752():
    t = input()
    hand = input().split()
    a = [i[0] for i in hand]
    b = [i[1] for i in hand]
    if t[0] in a or t[1] in b:
        print('YES')
    else:
        print('NO')