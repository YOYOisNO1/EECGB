def program841():
    n = int(input())
    s = [0]
    while True:
        for i in s:
            i *= 10
            if i + 4 >= n and str(i + 4).count('4') == str(4 + i).count('7') : print((i+4),) exit()
            elif i + 7 >= n and str(i + 7).count('4') == str(7 + i).count('7'): print((i+7),) exit()
            else: s.append(i+4), s.append(i+7)