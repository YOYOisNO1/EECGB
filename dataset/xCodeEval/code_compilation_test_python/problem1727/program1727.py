def program1727():
    li = [int(i) for i in input().split()]
    k = max(li)
    if(k == 6):
        print("0/1")
    elif(k == 1):
        print("1/1")
    else:
        d = 6-k+1
        if(d == 2):
            print("1/3")
        elif(d == 3):
            print("1/2")
        else(str(d)+"/"+"6")
        