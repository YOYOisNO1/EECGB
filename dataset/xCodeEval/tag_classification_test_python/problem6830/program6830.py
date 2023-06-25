def program6830():
    k = int(input())
    s = input()
    ans = ['' for _ in range(len(s))]
    r = set([chr(ord('a')+x) for x in range(k)]) - set(s)
    r = list(r)
    r.sort(reverse=True)
    
    c = 0
    for i in range(len(s)//2):
        if s[i] == '?' and s[-i - 1] == '?':
            c += 1
    if len(s) % 2 == 1 and s[len(s)//2] == '?':
        c += 1
    
    c -= len(r)
    for i in range(len(s)//2):
        if s[i] == '?' and s[-i-1] == '?':
            if c > 0:
                ans[i] = 'a'
                c -= 1
            else:
                ans[i] = r.pop()
            ans[-i-1] = ans[i]
        elif s[i] == '?':
            ans[i] = ans[-i-1] = s[-i-1]
        elif s[-i-1] == '?':
            ans[-i-1] = ans[i] = s[i]
        else:
            if s[i] == s[-i-1]:
                ans[i] = ans[-i-1] = s[i]
            else:
                print('IMPOSSIBLE')
                break
    else:
        if len(s) % 2 == 1:
            if s[len(s)//2] == '?':
                if r:
                    ans[len(s)//2] = r.pop()
                else:
                    ans[len(s)//2] = 'a'
            else:
                ans[len(s)//2] = s[len(s)//2]
        if r:
            print('IMPOSSIBLE')
        else:
            print(*ans, sep='')