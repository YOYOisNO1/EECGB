def program700():
    n=int(input())
    c=3
    for i in range(n):
        a=int(input())
        if a==c:
            print('NO')
            exit()
        c=6-a-c
    else:
        print('YES')