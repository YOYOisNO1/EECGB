def program6313():
    a, b, c, d = map(int, input().split())
    if a == b:
        print('Second')
    else:
        print('First' if a > b else 'Second')