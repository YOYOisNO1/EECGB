def program3689():
    a, b, r = map(int, input().split())
    r *= 2
    print('Second' if r > a or b < r else 'First')