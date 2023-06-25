def program1501():
    x = int(input())
    set = []
    y=x
    x = x + 1
    while x not in set:
        if x%10 == 0:
            x = x/10
        else:
            set.append(x)
            x+=1
                
    if y % 10 ==0 or (y+1)%10  == 0  y > 10:
        print(len(set)+1)
    else:
        print(len(set))