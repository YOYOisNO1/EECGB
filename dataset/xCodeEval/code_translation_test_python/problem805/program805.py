def program805():
    n = int(input())
    for i in range(n):
        t = int(input())
        if t%1111 == 0:
            print((t/1111)*10)
        elif t%111 == 0:
            print(((t/111)-1)*10) + 6
        elif t%11 == 0:
            print(((t/11)-1)*10) + 3
        else:
            print((t-1)*10) + 1