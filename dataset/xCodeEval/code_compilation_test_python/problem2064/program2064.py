def program2064():
    trash, n = [int(x) for x in input().split()]
    x = [str(x) for x in input().split()]
    s = list(x[0])
    done = False
    for i in range(len(s)):
        if s[i] == 'T' or s[i] == 'G':
            for j in range(i+n, len(s), n):
                if s[j] == 'T' or s[j] == 'G':
                    print('YES')
                    done = True
                    break
                if s[j] == '#':
                    print('NO')
                    done = True
                    break
            if done:
                break
    if not done:
        print('NO)