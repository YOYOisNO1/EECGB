def program1348():
    a = input()
    b1 = b2 = b3 = 0
    for i in range(0, len(a), 2):
       if a[i] == '1':
           b1 += 1
       elif a[i] == '2':
           b2 += 1
       else:
           b3 += 1
    aa = "1+" * b1 + "2+" * b2 + "3+" * b3
    print(aa[:-1]