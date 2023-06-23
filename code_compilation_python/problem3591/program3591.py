def program3591():
    import sys
    n = input()
    s = list(input())
    abc = sorted(set(('zyxwvutsrqponmlkjihgfedcba')[26-n:]) - set(s))
    sl = len(s)/2
    
    for i in xrange(sl):
        j = -i-1
        if s[i] == '?' and s[j] != '?': s[i] = s[j]
        elif s[j] == '?' and s[i] != '?': s[j] = s[i]
        elif s[i] != s[j]:
            print 'IMPOSSIBLE'
            sys.exit()
    
    sl += 1 if sl == 1
    for i in xrange(sl-1,-1,-1):
        if s[i] == '?':
            s[i] = s[-i-1] = abc.pop() if abc else 'a'
    
    
    print ''.join(s) if not abc else 'IMPOSSIBLE'
    