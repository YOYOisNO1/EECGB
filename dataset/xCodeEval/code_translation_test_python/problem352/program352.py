def program352():
    n = input()
    
    s = n
    while True:
        fl = False
        for i in range(2, n / 2 + 1):
            if n % i == 0:
                n = n / i
                s = s + n
                fl = True
                break
        if fl == False:
            s = s + 1
            break
    
    print(s)
    