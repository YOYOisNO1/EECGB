def program3174():
    n = int(input())
    k = 0
    if(n < 0):
        k = 1
        n = n * -1
    line = list(map(int,list(str(n))))
    if(k == 0):
        if (8 in line[:-1]) and (line[-1] < 9):
            print(1)
        else:
            if(line[-1] < 8):
                l = 8 - line[-1]
            elif(line[-1] == 8):
                l = 10
            else:
                l = 9
            jp = 10 - line[-1]
            if jp >= l:
                print(l)
            else:
                n = n + jp
                line = list(map(int,list(str(n))))
                if 8 in line:
                    print(jp)
                else:
                    print(l)
    elif(n <= 8):
        print(n+8)
    else:
        if (8 in line[:-1]) and (line[-1] != 0):
            print(1)
        else:
            if(line[-1] < 8):
                l = 2 + line[-1]
            elif(line[-1] == 8):
                l = 10
            else:
                l = 1
            jp = line[-1] + 1
            if jp >= l:
                print(l)
            else:
                n = n - jp
                if n < 0:
                    n = n * -1
                line = list(map(int,list(str(n))))
                if 8 in line:
                    print(jp)
                else:
                    print(l)