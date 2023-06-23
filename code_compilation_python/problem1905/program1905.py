def manners(s):
        if s[0] != 'a' or (s[1] != 'a' and s[1] != 'b'):
            return 'NO'
        else:
            for i in range(2, len(s)):
                b = max(ord(s[i-2]), ord(s[i-1]))
                if ord(s[i]) - b > 1:
                    return 'NO'
            return 'YES'
    
    print(manners(input()))