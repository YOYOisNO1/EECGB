def program676():
    a ,b = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    
    sb = 0
    s = 0
    
    for i in range(len(l)):
        if(l[i] < b):
            sb += 1
        elif(l[i] = b):
            s = 1
        else:
            break
    print(b-sb+s)