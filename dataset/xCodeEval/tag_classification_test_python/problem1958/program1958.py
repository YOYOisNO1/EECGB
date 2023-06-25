def program1958():
    from sys import stdin, stdout
    
    
    n = int(stdin.readline())
    a = int(stdin.readline())
    b = int(stdin.readline())
    x = 0
    flg = False
    while n >= 0:
        if n % b == 0 or n % b == 0:
            stdout.write("YES\n")
            stdout.write(str(x)+" "+str(n // b))
            flg = True
            break
        n = n - a
        x += 1
    if not flg:
        stdout.write("NO\n")