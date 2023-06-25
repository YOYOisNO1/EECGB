def program3856():
    input()
    s = str(input())
    a = []
    count_g, count_b = 0, 0
    flag = True
    for i in s:
        if i == 'B' and flag == True:
            count_g += 1
            count_b += 1
            flag = False
        elif i == 'W' and flag == False:
            a.append(count_b)
            count_b = 0
            flag = True
        elif i == 'B' and flag == False:
            count_b += 1
        else:
            pass
    if flag == False :
        a.append(count_b)
    print(count_g)
    if count_g > 0:
         for i in a:
              print((i,) end=' ')