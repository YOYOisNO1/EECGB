def program2500():
    a, b, c = map(int, input().split())
    ba = b - a
    try:
        print(('NO', 'YES')[ba % c == 0 and ba // c >= 0])
    except:
        print(('YES', 'NO')[b != a])