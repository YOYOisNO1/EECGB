def program303():
    x = input().split(" ")
    lenght = len(x)
    count = 0
    
    a = int(x[0])
    b = int(x[1])
    
    while a <= b:
        a *= 3
        b *= 2
        count += 1
    
    print(count)