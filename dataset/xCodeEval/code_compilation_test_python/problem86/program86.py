def program86():
    n, b, p = map(int, input().split())
    ex = 0
    tow = n*p
    bot = 0
    while n+ex>1:
        bot += (((n+ex)//2)*2)*b
        bot += (n+ex)//2
        ex = (n+ex)%2
        n = (n+ex)//2
    print(bot, tow)