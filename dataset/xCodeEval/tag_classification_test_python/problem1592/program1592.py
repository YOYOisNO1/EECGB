def program1592():
    x, y = input().split()
    i=1
    while x>=0 or y>=0:
        x=int(x)-i
        i=i+1
        if x>=0:
            y=int(y)-i
            i=i+1
        if x<0:
            break
        if y<0:
            break
            
    if x<0:
        print("Vladik")
    elif y<0:
        print("Valera")