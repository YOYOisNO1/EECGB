def program904():
    n = int(input())
    i = 0
    while (n >= 0):
        i += 1
        n -= i*(i+1)//2
    print(i-1)