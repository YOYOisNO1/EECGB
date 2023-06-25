def program2877():
    cod = input()
    ind = ["" for loop in range(10)]
    for i in range(10):
            ind[i] = input()
    
    ch =cod[i]
    for i in range(1,len(cod)):
        j = 0
        bol = False
        if i%10 == 0:
            while bol == False and j<10:
                if ind[j] == ch:
                    bol = True
                    print (j,end='')
                else:
                    j+=1
            
            ch = cod[i]
        else:
            ch += cod[i]
    j = 0
    bol = False
    while bol == False and j<10:
                if ind[j] == ch:
                    bol = True
                    print j
                else:
                    j+=1