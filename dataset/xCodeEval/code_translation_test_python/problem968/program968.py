def program968():
    from sys import stdin, stdout
    
    w, h = map(int, stdin.readline().split())
    
    if (w < 2 or h < 2):
        stdout.write('0')
    else:
        first = 0
        
        for i in range(w - 1):
            first += (w - i) // 2
        
        second = 0
        
        for i in range(1, h + 1):
            second += min(i, h - i)
        
        stdout.write(str(first * second))
            