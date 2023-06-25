def program3579():
    import fileinput;
    
    str = input();
    sstr = str.split(' ')
    a,b,w,x,c = int(sstr[0]),int(sstr[1]),int(sstr[2]),int(sstr[3]),int(sstr[4])
    
    dif = c-a
    count = 0
    while dif > 0:
        if (b >= x):
            factor = min(int((b - x)/x)+1,dif)
            dif = dif-factor
            b = b - x*factor
        else:
            count = count+1
            b = w - (x-b)
    
    print(count+(c-a))