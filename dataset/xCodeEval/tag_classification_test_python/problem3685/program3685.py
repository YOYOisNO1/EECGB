def program3685():
    array = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday", "tuesday", "wednesday"]
    x = input()
    y = input()
    if x == y:
        print("YES")
    else:
        for i in range(len(array)):
            try:
                if x == array[i] and y == array[i+2]:
                    print("YES")
                    break
                elif x == array[i] and y == array[i+3]:
                    print("YES")
                    break
            except: pass
        else:
            print("NO")