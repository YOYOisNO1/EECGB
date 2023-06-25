def isPalindrom(s):
        return s == s[::-1]
    
    s = input()
    max = 0
    for i in range(len(s) - 1):
        for j in range(i+1, len(s) + 1):
            #print(s[i:j])
            if isPalindrom(s[i:j]) == False:
                if len(s[i:j]) > max:
                    max = len(s[i:j])
    
    
    
    print(max)