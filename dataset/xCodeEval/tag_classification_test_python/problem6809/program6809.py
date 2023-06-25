def program6809():
    from sys import stdin, stdout
    
    k = int(stdin.readline())
    s = list(stdin.readline().strip())
    used = [0 for i in range(k)]
    
    for f in s:
        if f != '?':
            used[ord(f) - ord('a')] = 1
    
    
    cnt = 0
    for i in range(len(s)):
        if s[i] != '?' and s[-i - 1] != '?' and s[i] != s[-i - 1]:
            stdout.write('IMPOSSIBLE')
            break
        
        if s[i] != s[-i - 1]:
            s[i] = chr(max(ord(s[i]), ord(s[-i - 1])))
            s[-i - 1] = chr(max(ord(s[i]), ord(s[-i - 1])))
        
        if s[i] == s[-i - 1] == '?':
            cnt += 1
    else:
        cnt = cnt % 2 + cnt // 2
        may = cnt - used.count(0)
        
        if may < 0:
            stdout.write('IMPOSSIBLE')
        else:
            for i in range(len(s)):
                if s[i] == '?':
                    if may:
                        s[i] = 'a'
                        s[-i - 1] = 'a'
                        if not used[0]:
                            used[0] = 1
                        else:
                            may -= 1
                    else:
                        s[i] = chr(used.index(0) + ord('a'))
                        s[-i - 1] = chr(used.index(0) + ord('a'))
                        used[used.index(0)] = 1
                        
            stdout.write(''.join(s))