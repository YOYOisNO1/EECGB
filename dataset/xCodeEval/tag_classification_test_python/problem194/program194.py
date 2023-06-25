def program194():
    n, d = map(int, input().split())
    s = input()
    x = 0
    go = 0
    hear = 0
    MIN = 0
    i = 0
    while i < len(s):
        i+=1
        x+=1
        if x < d:
            if s[i] == '1':
                go = i
                if i == n-1:
                    MIN+=1
                    print(MIN)
                    break
        elif x == d:
            if s[i] == '1' and i == n-1:
                MIN+=1
                print(MIN)
                break
            elif s[i] == '1':
                go = i
            if hear != go:
                hear = go
                i = go
                MIN+=1
            else:
                print('-1')
                break
            x = 0