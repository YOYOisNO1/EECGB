def program579():
    x = input()
    i = 2
    s = 'NO'
    while (i <= x-2):
        if ((x-i)%2 == 0):
            s = 'YES'
            break
        i = i+2
    print(s)