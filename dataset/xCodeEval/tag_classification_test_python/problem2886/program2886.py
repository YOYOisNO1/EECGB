def program2886():
    n = int(input())
    string = input()
    choose = ['jolteon','flareon','umbreon','leafeon','glaceon','sylveon']
    list = []
    if n == 8:
        print('vaporeon')
    elif n == 6:
        print('espeon')
    elif n == 7:
        for i in choose:
            k = 0
            for j in range(7):
                if string[j]=='.':
                    pass
                else:
                    if i[j] != string[j]:
                        k = 1
                        break
                
            if k == 0:
                list.append(i)
    for i in list:
        print(i)