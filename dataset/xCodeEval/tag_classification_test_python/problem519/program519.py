def program519():
    tmp = input()
    a, b, c = tmp.split(' ')
    a, b, c = int(a), int(b), int(c)
    ans = ((a - 1) // c + 1) * ((b - 1) // c + 1)
    print(ans)