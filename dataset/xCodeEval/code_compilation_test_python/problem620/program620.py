def IsBerlanese():
        s = input()
        vowels = 'aeiou'
        i = 0
        while i < len(s)-1:
            if s[i] not in vowels and s[i] != 'n':
                if s[i+1] not in vowels:
                    return 'NO'
            i += 1
        
        if s[i] == 'n' or s[i] in vowels:
            return 'YES'
        else:
            return 'NO'
        
    print IsBerlanese()