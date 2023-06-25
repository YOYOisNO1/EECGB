    import sys
    import copy
    list = []   #定义一个空列表
    dice={str(i):[] for i in range(0,10)}
    i=-1
    for line in sys.stdin:
        i+=1
        if i==0:
            n=int(line)
        else:
            list_new = line.split()
            for j in list_new:
                dice[j].append(i)
    
    
    if n=='0':
        print("0")
        exit()
    x=1
    while True:
        y=str(x)
        choice = [] # 用choice 存储每个number备选的骰子
        for k in y:
            choice.append(copy.deepcopy(dice[k]))
        if len(choice) < len(y):
            print(x)
            exit()
        while choice != []:
            if choice[0]==[]:
                print(x-1)
                exit()
            else:
                hash=[]
                # if y=="18":
                #     print(dice)
                for r in choice[0]:
                    h=0
                    for g in range(1, len(choice)):
                        if r in choice[g]:
                            h+=1
                    hash.append((r,h))
    
            def by_name(t):
                    return t[1]
                digit=sorted(hash, key=by_name)[0][0]
                for g in range(1, len(choice)):
                    if digit in choice[g]:
                        choice[g].remove(digit)
                choice.remove(choice[0])
    
        x+=1
    