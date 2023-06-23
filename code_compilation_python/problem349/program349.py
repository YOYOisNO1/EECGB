def program349():
    n = int(input())
    s = input().strip()
    f = False
    for i in range(n):
        for j in range(n):
            x = j
            c = 0
            while x < n:
                if s[x] == '*':
                    c += 1
                else:
                    c = 0
                if c == 4:
                    f = True
                x += i
    if f:
        print('yes')
    else:
        print('no')