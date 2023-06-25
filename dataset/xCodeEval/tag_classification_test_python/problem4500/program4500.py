def program4500():
    from sys import stdin, stdout
    
    
    s = stdin.readline().strip()
    ans = list(s)
    current = 0
    
    patern = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i] <= patern[current]:
            ans[i] = patern[current]
            current += 1
        
        if current == len(patern):
            stdout.write(''.join(ans))
            break
    else:
        stdout.write('-1')