def program110():
    s = input()
    
    l = list()
    ip = -1
    
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
            val = i
            l.append(val - ip)
            ip = val
    
    l.append(len(s) - ip)
    
    print(max(l))