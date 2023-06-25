def program3777():
    n = int(input())
    s = input()
    c = s.count('0')
    j = 0
    if s == '0':
        print(0)
    else:
        print(1, end='')
        while j < c:
            print(0, end = '')
            j += 1