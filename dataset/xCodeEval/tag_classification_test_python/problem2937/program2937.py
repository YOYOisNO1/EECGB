def program2937():
    x1, y1 = map(int,input().split(' '))
    x2, y2 = map(int,input().split(' '))
    x3, y3 = map(int,input().split(' '))
    s = 0
    my_list = []
    x4 = (x2-x1+x3)
    y4 = (y2-y1+y3)
    if (((x4-x3)**2+(y4-y3)**2)**(0.5) == ((x2-x1)**2+(y2-y1)**2)**(0.5)) and (((x4-x2)**2+(y4-y2)**2)**(0.5) == ((x3-x1)**2+(y3-y1)**2)**(0.5)):
        s = s+1
        my_list.append(x4)
        my_list.append(y4)
    x4 = (x1-x2+x3)
    y4 = (y1-y2+y3)
    if (((x4-x3)**2+(y4-y3)**2)**(0.5) == ((x2-x1)**2+(y2-y1)**2)**(0.5)) and (((x3-x2)**2+(y3-y2)**2)**(0.5) == ((x4-x1)**2+(y4-y1)**2)**(0.5)):
        s = s+1
        my_list.append(x4)
        my_list.append(y4)  
    x4 = (x2-x3+x1)
    y4 = (y2-y3+y1)
    if (((x4-x1)**2+(y4-y1)**2)**(0.5) == ((x2-x3)**2+(y2-y3)**2)**(0.5)) and (((x4-x2)**2+(y4-y2)**2)**(0.5) == ((x3-x1)**2+(y3-y1)**2)**(0.5)):
        s = s+1
        my_list.append(x4)
        my_list.append(y4)  
    print(s)
    while len(my_list)>0:
        print(my_list[0],) my_list[1]
        my_list = my_list[2:len(my_list)]