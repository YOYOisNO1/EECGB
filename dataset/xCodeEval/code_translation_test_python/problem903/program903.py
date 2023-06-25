def t_in_sub(sub, t):
        j = i = 0
        while i<len(sub) and j<len(t):
            if t[j] == sub[i]:
                j+=1
            i+=1
        if j == len(t):
            return True
        return False
    
    s = input()
    t = input()
    mx = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[:i]+s[j+1:]
            if t_in_sub(sub, t):
                mx = max(mx, j-i+1)
    print(mx)