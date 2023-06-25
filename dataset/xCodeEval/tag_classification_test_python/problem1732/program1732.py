def program1732():
    num = map(int,input().split())
    strr = ""
    str_dez = "1"
    if num[0] == 1 and num[1] == 10:
        print("-1")
    elif num[1] < 10:
        for i in range(num[0]):
            strr += str(num[1])
        print(strr)
    else:
        if num[1] == 10:
            for k in range(1,num[0]):
                str_dez += "0"
            print(str_dez)