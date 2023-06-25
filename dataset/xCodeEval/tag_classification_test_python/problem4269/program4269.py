def program4269():
    a = input()
    b=a
    count=0
    while True:
        b=b[-1]+b[0:-1]
        count+=1
        if b==a:
            break
    print(count)