def program2788():
    import math
    
    x, y, n = input().split()
    x = int(x)
    y = int(y)
    n = int(n)
    new = 2
    
    if y <= n:
        print(str(x) + '/' + str(y))
    else:
        for i in range(1, n+1):
            fraction = x / y
            up = fraction * i
            up1 = math.ceil(up)
            up2 = math.floor(up)
            a = abs(up1 / i - x / y)
            b = abs(up2 / i - x / y)
            if a > b and b < new:
                new = b
                uup = up2
                ddo = i
            elif a < b and a < new:
                new = a
                uup = up1
                ddo = i
            #elif a = b<new:
             #   new = a
              #  uup = up2
               # ddo = i
                #和第一个if结合起来就好 第一个的第一个比较运算符从>变成>=
    
        print(str(uup) + '/' + str(ddo))