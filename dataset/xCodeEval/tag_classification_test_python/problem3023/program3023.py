def program3023():
    n = int(input())
    #n, m = map(int, input().split())
    #s = input()
    #c = list(map(int, input().split()))
    a = []
    while n != 0:
        s = str(n)
        t = ''
        for i in range(len(s)):
            if s[i] != '0':
                t += '1'
            else:
                t += '0'
        a.append(t)
        n -= int(t)
    print(len(a))
    print(*a)