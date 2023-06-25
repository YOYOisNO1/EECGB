def program4056():
    s = str(input())
    
    if (s.find('e') == -1):
        frac = int(s[s.find('.') + 1:])
        if frac == 0:
            tmp = s[:s.find('.')]
            s = tmp
        
        print(s)
    else:
        if s.find('.') != -1:
            frac = int(s[s.find('.') + 1:s.find('e')])
            if frac == 0:
                tmp = s[:s.find('.')] + s[s.find('e'):]
                s = tmp
        
        ans = s[:s.find('e')]
        pt = s.find('.')
        m = int(s[s.find('e') + 1:])
    
        if pt == -1:
            for i in range(m):
                ans += '0'
            print(ans)
        else:
            ln = len(ans) - (pt + 1)
            if ln > m:
                print(s[:pt]) + s[pt + 1:pt + m + 1] + '.' + s[pt + m + 1:s.find('e')]
            else:
                ans = s[:pt] + s[pt + 1:s.find('e')]
                for i in range(m - ln):
                    ans += '0'
                print(ans)