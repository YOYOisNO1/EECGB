def program176():
    t = int(input())
    while t:
        n1, n2 = map(int,input().split())
        rev = 0
        while n2 > 0:
            rem = n2 % 10
            rev = (rev * 10) + rem
            n2 = n2 // 10
        print(f'{n1 + rev}')
        t = t - 1