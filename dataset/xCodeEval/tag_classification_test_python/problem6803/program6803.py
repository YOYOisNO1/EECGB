def program6803():
    import sys
    
    k = int(input())
    s = list(input())
    used = [False] * k
    for i in range(len(s)):
        if '?' not in (s[i], s[-i - 1]) and \
                s[i] != s[-i - 1]:
            print('IMPOSSIBLE')
            sys.exit(0)
        if s[i] != '?':
            if s[-i - 1] == '?':
                s[-i - 1] = s[i]
            used[ord(s[i]) - ord('a')] = True
    
    if len(s) % 2 and s[len(s) // 2] == '?':
        doUnused = True
        for j in range(k - 1, -1, -1):
            if not used[j]:
                s[len(s) // 2] = chr(ord('a') + j)
                used[j] = True
                doUnused = False
                break
        if doUnused:
            s[len(s) // 2] = 'a'
    for i in range((len(s) - 2) // 2, -1, -1):
        if s[i] == '?':
            doUnused = True
            for j in range(k - 1, -1, -1):
                if not used[j]:
                    s[i] = chr(ord('a') + j)
                    s[-i - 1] = s[i]
                    used[j] = True
                    doUnused = False
                    break
            if doUnused:
                s[i] = 'a'
                s[-i - 1] = 'a'
    
    if not all(used):
        print('IMPOSSIBLE')
    else:
        print(''.join(s))
    