def program3037():
    str1 = input();
    str2 = input();
    list1=  []
    list1.append(str1[0])
    list1.append(str1[1])
    list1.append(str2[1])
    list1.append(str2[0])
    for i in xrange(4):
        if list1[i] == 'X':
            del list1[i]
    str1 = input();
    str2 = input();
    list2=  []
    list2.append(str1[0])
    list2.append(str1[1])
    list2.append(str2[1])
    list2.append(str2[0])
    for i in xrange(4):
        if list2[i] == 'X':
            del list2[i]
            break
    for i in xrange(3):
        if list1[0] != list2[0]:
            temp = list1[0]
            del list1[0]
            list1.append(temp);
    if list1[0] == list2[0] and list1[1] == list2[1]:
        print 'YES'
    else:
        print 'NO'