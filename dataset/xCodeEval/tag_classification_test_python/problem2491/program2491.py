def program2491():
    s = input() + input() + input()
    if s == s[::-1]:
        print('YES')
    else:
        print('NO')