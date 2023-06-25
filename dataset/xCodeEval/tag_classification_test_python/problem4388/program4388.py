def program4388():
    from sys import stdin, stdout
    
    s = list(stdin.readline().strip())
    
    i = 1
    while i < len(s) - 3:
        if ''.join(s[i:i + 3]) == 'dot':
            s = s[:i] + ['.'] + s[i + 3:]
        i += 1
    
    i = 1
    while i < len(s) - 2:
        if ''.join(s[i:i + 2]) == 'at':
            s = s[:i] + ['@'] + s[i + 2:]
            break
        i += 1
    
    stdout.write(''.join(s))