def program1227():
    s = input()
    
    s = s.replace('at', '@', 1)
    
    if s[0] == '@':
        s = 'at' + s[1:].replace('at', '@', 1)
    
    if s.count('dot'):
        s = s.replace('dot', '.')
        if s[0] == '.':
            s = s.replace('.', 'dot', 1)
        if s[-1] == '.':
            s = s[:len(s)-1] + 'dot'
                
    print(s)