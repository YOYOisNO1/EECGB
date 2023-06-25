def program873():
    n = int(input())
    slist = input()
    slist += '0'
    c = 0
    ans = ''
    for s in slist:
        if s == '0':
            ans += str(c)
            c = 0
        else: c += 1
    print(ans)