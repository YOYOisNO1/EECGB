def program1953():
    n = input()
    F_a = input()
    mass_1 = []
    mass_2 = []
    mas = []
    for i in F_a:
        mass_1.append(int(i))
    
    for i in mass_1:
        if i == 2:
           mas = [2]
           if len(mass_2) > 0:
                for j in mas:
                    flag = True
                    for y in range(len(mass_2)):
                        if j >= mass_2[y]:
                            mass_2.insert(y, j)
                            flag = False
                            break
                    if flag:
                        mass_2.append(j)
    
           else:
               mass_2.append(2)
        elif i == 3:
            mas = [3]
            if len(mass_2) > 0:
                for j in mas:
                    flag = True
                    for y in range(len(mass_2)):
                        if j >= mass_2[y]:
                            mass_2.insert(y, j)
                            flag = False
                            break
                    if flag:
                        mass_2.append(j)
    
            else:
                mass_2.append(3)
        elif i == 4:
            mas = [3, 2, 2]
            if len(mass_2) > 0:
                for j in mas:
                    flag = True
                    for y in range(len(mass_2)):
                        if j >= mass_2[y]:
                            mass_2.insert(y, j)
                            flag = False
                            break
                    if flag:
                        mass_2.append(j)
    
            else:
                mass_2.append(3)
                mass_2.append(2)
                mass_2.append(2)
        elif i == 5:
            mas = [5]
            if len(mass_2) > 0:
                for j in mas:
                    flag = True
                    for y in range(len(mass_2)):
                        if j >= mass_2[y]:
                            mass_2.insert(y, j)
                            flag = False
                            break
                    if flag:
                        mass_2.append(j)
    
            else:
                mass_2.append(5)
        elif i == 6:
            mas = [5, 3]
            if len(mass_2) > 0:
                for j in mas:
                    flag = True
                    for y in range(len(mass_2)):
                        if j >= mass_2[y]:
                            mass_2.insert(y, j)
                            flag = False
                            break
                    if flag:
                        mass_2.append(j)
    
            else:
                mass_2.append(5)
                mass_2.append(3)
        elif i == 7:
            mas = [7]
            if len(mass_2) > 0:
                for j in mas:
                    flag = True
                    for y in range(len(mass_2)):
                        if j >= mass_2[y]:
                            mass_2.insert(y, j)
                            flag = False
                            break
                    if flag:
                        mass_2.append(j)
    
            else:
                mass_2.append(7)
        elif i == 8:
            mas = [7, 2, 2, 2]
            if len(mass_2) > 0:
                for j in mas:
                    flag = True
                    for y in range(len(mass_2)):
                        if j >= mass_2[y]:
                            mass_2.insert(y, j)
                            flag = False
                            break
                    if flag:
                        mass_2.append(j)
    
            else:
                mass_2.append(7)
                mass_2.append(2)
                mass_2.append(2)
                mass_2.append(2)
        elif i == 9:
            mas = [7, 3, 3, 2]
            if len(mass_2) > 0:
                for j in mas:
                    flag = True
                    for y in range(len(mass_2)):
                        if j >= mass_2[y]:
                            mass_2.insert(y, j)
                            flag = False
                            break
                    if flag:
                        mass_2.append(j)
            else:
                mass_2.append(7)
                mass_2.append(3)
                mass_2.append(3)
                mass_2.append(2)
    a = ''
    for i in mass_2:
        a = a + str(i)
    print(a)