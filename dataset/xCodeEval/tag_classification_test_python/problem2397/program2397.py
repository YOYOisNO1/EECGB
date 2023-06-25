def program2397():
    s = input()
    if '4' not in s and '7' not in s: print(-1)
    else:
        a4 = s.count('4')
        a7 = s.count('7')
        if a4==a7:
            print(4)
        else:
            print('4' if a4>a7 else '7')