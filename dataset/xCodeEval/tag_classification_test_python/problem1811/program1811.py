def program1811():
    
    options = []
    great = [0]*4
    for line in range(4):
        options.append(input().split("."))
    
    for i in range(4):
        options2 = options[:]
        y = options2.pop(i)
        short = True
        for o in options2: 
            if len(y[1]) <= len(o[1])/2:
                pass
            else:
                short = False
                break
        large = True
        for k in options2:
            if len(y[1]) >= len(k[1])*2:
                pass
            else:
                large = False
                break
        #print(short, large)
        if short or large:
            great[i] = 1
    
    if sum(great) == 1:
        print(options[great.index(1)][0])
    else:
        print("C")