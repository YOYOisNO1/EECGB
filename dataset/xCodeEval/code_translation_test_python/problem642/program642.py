def program642():
    s = input()
    s = input().lower()
    fl = sum(map(lambda x: s.find(x) >= 0, list('qazwsxedcrfvtgbyhnujmikolp'))) == 26
    if fl:
        print('YES')
    else:
        print('NO')