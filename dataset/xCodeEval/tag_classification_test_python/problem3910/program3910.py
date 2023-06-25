def program3910():
    l = map(int, input().split())
    a = l[0]
    b = l[1]
    if (a == 2):
        print("YES")
    else:
        flag = True
        while (b > 0):
            if (b%a == 1):
                b -= 1
                b /= a
            elif (b%a == a-1):
                b += 1
                b /= a
            elif (b%a == 0):
                b /= a
            else:
                flag = False
                b = 0
        if flag:
            print("YES")
        else:
            print("NO")
        
        
        