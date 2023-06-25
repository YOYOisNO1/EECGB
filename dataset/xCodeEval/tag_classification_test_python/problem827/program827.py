def program827():
    s = input()
    l = 0
    r = 0
    alphabet = [0]*26
    quest = 0
    if (s[r] == '?'):
        quest += 1
    else:
        alphabet[ord(s[0])-65] = 1
    
    length = len(s)
    while True:
        r += 1
        if (r == length):
            r -= 1
            break
        if (s[r] == '?'):
            quest+=1
        elif (alphabet[ord(s[r])-65] == 1):
            l = r
            quest = 0
            alphabet = [0]*26
            if s[r] == '?':
                quest += 1
            alphabet[ord(s[r])-65] = 1
            while (s[l-1] != s[r]):
                if s[l-1] == '?':
                    quest += 1
                else:
                    alphabet[ord(s[l-1])-65] = 1
                l -= 1
        else:
            alphabet[ord(s[r])-65] = 1
        if (r-l == 25):
            break
    
    if (r - l  != 25):
        print(-1)
    else:
        res = ""
        for i in range(0, l):
            if s[i] != '?':
                res += s[i]
            else:
                res += 'A'
        for i in range(l, r+1):
            if s[i] != '?':
                res += s[i]
            else:
                for i in range(0,26):
                    if (alphabet[i] == 0):
                        res += chr(i+65)
                        alphabet[i] = 1
                        break
        for i in range(r+1, len(s)):
            if s[i] != '?':
                res += s[i]
            else:
                res += 'A'
        print(res)