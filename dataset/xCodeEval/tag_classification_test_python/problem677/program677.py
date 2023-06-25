    data = input()
    data = data.split()
    data = list(map(int, data))
    a = data[0]
    b = data[1]
    x = data[2]
    y = data[3]
    
    
def gcd(a, b):
        if a < b:
            a, b = b, a
        y = a % b
        if  y == 0:
            return b
        else:
            a, b = b, y
            return gcd(a,b)
    
    t = gcd(x,y)
    x = x/t
    y = y/t
    time = int(min([a//x,b//y]))
    print(time)
    