def program1929():
    s = input()
    s = input().lower()
    fl = sum(map(lambda x: s.find(x) >= 0, map(lambda x : chr(x + ord('a')), range(0,26)))) == 26
    if fl:
        print('YES')
    else:
        print('NO')